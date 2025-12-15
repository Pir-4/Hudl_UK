import json
import logging

from base.config import LOGGER_LEVEL


class BaseLogger:
    def __init__(self, logger_name=None):
        self.logger_name = logger_name or self.__class__.__name__
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(LOGGER_LEVEL)

    @staticmethod
    def _format_message(data):
        if isinstance(data, str):
            try:
                json_data = json.loads(data)
                return json.dumps(json_data, indent=3, ensure_ascii=True)
            except json.JSONDecodeError:
                pass

        elif isinstance(data, dict):
            try:
                return json.dumps(data, indent=3, ensure_ascii=False)
            except TypeError:
                pass

        return data

    def _logging_msg(self, logg_func, msg, data=None):
        result_string = f'[{self.logger_name}] {msg}'

        if data:
            formated_data = self._format_message(data)
            result_string += f' {formated_data}'

        logg_func(result_string)

    def debug(self, msg, data=None):
        self._logging_msg(self.logger.debug, msg, data)

    def info(self, msg, data=None):
        self._logging_msg(self.logger.info, msg, data)

    def warning(self, msg, data=None):
        self._logging_msg(self.logger.warning, msg, data)

    def error(self, msg, data=None):
        self._logging_msg(self.logger.error, msg, data)

    def critical(self, msg, data=None):
        self._logging_msg(self.logger.critical, msg, data)


logger = BaseLogger()
