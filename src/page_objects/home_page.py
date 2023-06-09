import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(HomePage, self).__init__(driver, wait_driver)

    def search(self, value: str):
        logging.info(f"Search {value}")
        self.element("search_input").wait_clickable().send_keys(value)
        self.element("search_btn").wait_clickable().click()

    def obtain_menu_elements(self) -> list[str]:
        logging.info(f"Get menu bar names")
        self.element("menu_bar").wait_visible()
        return [element.text for element in self.element("menu_bar").find_elements()]

