import pytest

from src.factory.webdriver_factory import get_drivers


@pytest.fixture(autouse=True)
def web_drivers():
    driver, wait_driver = get_drivers()
    yield driver, wait_driver
    driver.quit()
    # with open("screenshots/test_invalid_login.png", "w") as screenshot_file:
    #     driver.save_screenshot(screenshot_file)
    #     driver.quit()