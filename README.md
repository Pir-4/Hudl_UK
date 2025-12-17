# Hudl UK

A comprehensive Selenium-based automated testing framework for testing Hudl login functionality using Python and pytest. The framework follows the Page Object Model (POM) pattern for maintainable and scalable test automation.

## Overview

This project contains automated tests for the Hudl website login functionality, including:
- Happy path login scenarios
- Email input validation
- Password input validation
- Username editing functionality

## Features

- **Page Object Model (POM)**: Clean separation of page logic and test code
- **Multi-browser Support**: Chrome, Firefox, Edge, and Safari
- **Comprehensive Test Coverage**: Multiple validation scenarios with parameterized tests
- **Custom Logging**: Structured logging with configurable log levels
- **Reusable Steps**: Common test steps extracted for reusability
- **Environment-based Configuration**: Environment variables for flexible configuration

## Project Structure

```
Hudl_UK/
├── base/                           # Core framework code
│   ├── asserts/                    # Custom assertion helpers
│   │   ├── base_asserts.py
│   │   └── page_asserts.py
│   ├── pages/                      # Page Object classes
│   │   ├── base_page.py           # Base page with common functionality
│   │   ├── browsers.py            # Browser factory
│   │   ├── login_page.py          # Login page object
│   │   ├── main_page.py           # Main page object
│   │   └── user_home_page.py      # User home page object
│   ├── config.py                  # Configuration management
│   ├── logger.py                  # Custom logging implementation
│   └── steps.py                   # Reusable test steps
├── tests/                          # Test files
│   ├── conftest.py                # Pytest configuration and fixtures
│   └── login/                     # Login test suite
│       ├── conftest.py            # Test-specific fixtures
│       ├── constants.py           # Test constants
│       ├── asserts.py             # Test-specific assertions
│       └── test_login.py          # Login test cases
├── requirements.txt               # Python dependencies
├── pytest.ini                    # Pytest configuration
└── README.md                     # This file
```

## Requirements

- Python 3.11+
- pip (Python package manager)
- WebDriver for your chosen browser (Chrome, Firefox, Edge, or Safari)

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd Hudl_UK
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install WebDriver**:
   - **Chrome**: Download [ChromeDriver](https://chromedriver.chromium.org/)
   - **Firefox**: Download [GeckoDriver](https://github.com/mozilla/geckodriver/releases)
   - **Edge**: Download [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
   - **Safari**: Enable "Allow Remote Automation" in Safari's Develop menu

   Make sure the WebDriver executable is in your system PATH or specify its location in your environment.

## Configuration

Create a `.env` file in the project root directory with the following environment variables:

```env
# Required
TEST_EMAIL=your_test_email@example.com
TEST_PASSWORD=your_test_password

# Optional (with defaults)
TARGET_URL=https://hudl.com/
BROWSER_NAME=chrome
LOGGER_LEVEL=INFO
```

### Environment Variables

| Variable        | Required | Default             | Description                                                    |
| --------------- | -------- | ------------------- | -------------------------------------------------------------- |
| `TEST_EMAIL`    | Yes      | -                   | Email address for testing login                                |
| `TEST_PASSWORD` | Yes      | -                   | Password for testing login                                     |
| `TARGET_URL`    | No       | `https://hudl.com/` | Target website URL                                             |
| `BROWSER_NAME`  | No       | `chrome`            | Browser to use: `chrome`, `firefox`, `edge`, or `safari`       |
| `LOGGER_LEVEL`  | No       | `INFO`              | Logging level: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` |

## Running Tests

### Run all tests:
```bash
pytest
```

### Run specific test file:
```bash
pytest tests/login/test_login.py
```

### Run specific test:
```bash
pytest tests/login/test_login.py::test_login_happy_path
```

### Run with verbose output:
```bash
pytest -v
```

### Run with detailed output:
```bash
pytest -vv
```

### Run tests in parallel (if pytest-xdist is installed):
```bash
pytest -n auto
```

## Test Cases

The framework includes the following test scenarios:

1. **test_login_happy_path**: Tests successful login flow
2. **test_email_input_validation**: Parameterized tests for email validation with various input scenarios
3. **test_password_input_validation**: Parameterized tests for password validation
4. **test_edit_username**: Tests the username editing functionality

### Email Validation Test Cases

The email validation tests cover:
- Valid email formats (standard, with numbers, with punctuation, complex domains)
- International domains (punycode and local language)
- Invalid formats (missing @, incomplete domains, wrong domain size)
- Edge cases (empty strings, web addresses without @)

### Password Validation Test Cases

The password validation tests cover:
- Valid credentials
- Wrong password
- Wrong email with valid password
- Empty password

## Technologies Used

- **Python 3.11+**: Programming language
- **Selenium 4.39.0**: Web browser automation
- **pytest 9.0.2**: Testing framework
- **python-dotenv 1.2.1**: Environment variable management
- **environs 14.5.0**: Environment variable parsing and validation

## Pytest Configuration

The `pytest.ini` file includes:
- Strict markers enabled
- Test timeout: 10 seconds
- CLI logging enabled with formatted timestamps

## Logging

The framework includes a custom logging implementation that:
- Supports configurable log levels
- Formats JSON data for readability
- Provides structured log messages with class names
- Outputs timestamps and log levels

## Contributing

1. Follow the Page Object Model pattern for new page objects
2. Add appropriate assertions using the custom assertion helpers
3. Extract reusable steps to `base/steps.py`
4. Write descriptive test names and include docstrings where helpful
5. Ensure tests are parameterized when testing multiple scenarios

## Notes

- Tests include a 10-second timeout as configured in `pytest.ini`
- The framework automatically handles privacy/cookie consent windows
- WebDriver instances are properly managed through pytest fixtures
