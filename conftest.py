import logging
import os.path
import pathlib

import pytest

from src.factory.webdriver_factory import get_drivers

_SCREENSHOT_PATH = os.path.join(pathlib.Path(__file__).parent, "screenshots")


@pytest.fixture(autouse=True)
def web_drivers(request):
    caller = request.node.name
    driver, wait_driver = get_drivers()
    yield driver, wait_driver
    try_take_screenshot(driver, caller)
    driver.quit()


def try_take_screenshot(driver, test_name):
    try:
        file_path = os.path.join(_SCREENSHOT_PATH, f"{test_name}.png")
        driver.save_screenshot(file_path)
    except:
        logging.error(f"cannot save screenshot after execution of {test_name}")