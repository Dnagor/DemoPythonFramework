import logging as log

from msedge.selenium_tools.webdriver import WebDriver
from pypom import Page
from selenium.webdriver.common.by import By


class PracticePage(Page):
    _radio_button_one = (By.XPATH, "//input[@value='radio1']")
    _radio_button_list = (By.ID, "radio-btn-example")
    _hide_show_input = (By.ID, "displayed-text")
    _show_button = (By.ID, "show-textbox")
    _hide_button = (By.ID, "hide-textbox")
    _name_input = (By.ID, "name")
    _alert_button = (By.ID, "alertbtn")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def select_radio_button_one(self):
        self.driver.find_element(*self._radio_button_one).click()
        log.info("Clicked radio option one")

    def select_radio_button_by_name(self, radio: str):
        radio_buttons = self.driver.find_element(*self._radio_button_list).find_elements(By.CSS_SELECTOR, "input")
        for button in radio_buttons:
            if button.get_attribute("value").lower() == radio.lower():
                button.click()
        log.info(f"Clicked radio option wiht name: {radio}")

    def hide_text(self):
        self.driver.find_element(*self._hide_button).click()
        log.info("Clicked hide text")

    def show_text(self):
        self.driver.find_element(*self._show_button).click()
        log.info("Clicked show text")

    def input_text(self, text: str):
        self.driver.find_element(*self._hide_show_input).send_keys(text)
        log.info(f"Entered text: {text}")

    def get_text(self) -> str:
        text = self.driver.find_element(*self._hide_show_input).get_attribute("value")
        log.info(f"Received folloving text: {text}")
        return text

    def is_text_displayed(self) -> bool:
        displayed = self.driver.find_element(*self._hide_show_input).is_displayed()
        log.info("Text is {}".format("displayed" if displayed else "not displayed"))
        return displayed

    def input_name(self, name: str):
        self.driver.find_element(*self._name_input).send_keys(name)
        log.info(f"Entered name: {name}")

    def click_alert_button(self):
        self.driver.find_element(*self._alert_button).click()
        log.info("Clicked alert button")

    def get_text_from_alert(self) -> str:
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.dismiss()
        self.driver.switch_to.default_content()
        log.info(f"Received text from alert: {text}")
        return text

    def get_name(self) -> str:
        name = self.driver.find_element(*self._hide_show_input).get_attribute("value")
        log.info(f"Received name: {name}")
        return name
