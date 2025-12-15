from selenium import webdriver


def get_browser(browser_name: str):
    """
    Return a Selenium WebDriver instance based on the given browser name.

    Supported values (case-sensitive):
      - 'chrome'
      - 'firefox'
      - 'edge'
      - 'safari'
    """
    match browser_name.lower():
        case "chrome":
            return webdriver.Chrome()
        case "firefox":
            return webdriver.Firefox()
        case "edge":
            return webdriver.Edge()
        case "safari":
            return webdriver.Safari()
        case _:
            raise ValueError(
                "Browser name must be one of: 'chrome', 'firefox', 'edge', or 'safari'"
            )
