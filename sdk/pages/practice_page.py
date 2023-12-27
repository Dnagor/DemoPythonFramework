from msedge.selenium_tools.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pypom import Page


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

    def select_radio_button_by_name(self, radio: str):
        radio_buttons = self.driver.find_element(*self._radio_button_list).find_elements(By.CSS_SELECTOR, "input")
        for button in radio_buttons:
            if button.get_attribute("value").lower() == radio.lower():
                button.click()

    def hide_text(self):
        self.driver.find_element(*self._hide_button).click()

    def show_text(self):
        self.driver.find_element(*self._show_button).click()

    def input_text(self, text: str):
        self.driver.find_element(*self._hide_show_input).send_keys(text)

    def get_text(self) -> str:
        return self.driver.find_element(*self._hide_show_input).get_attribute("value")

    def is_text_displayed(self) -> bool:
        return self.driver.find_element(*self._hide_show_input).is_displayed()

    def input_name(self, name: str):
        self.driver.find_element(*self._name_input).send_keys(name)

    def click_alert_button(self):
        self.driver.find_element(*self._alert_button).click()

    def get_text_from_alert(self) -> str:
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.dismiss()
        self.driver.switch_to.default_content()
        return text

    def get_name(self) -> str:
        return self.driver.find_element(*self._hide_show_input).get_attribute("value")
