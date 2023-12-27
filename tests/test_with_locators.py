import pytest
from pytest import mark

from sdk.pages.practice_page import PracticePage
from tests import PROPERTIES


@pytest.mark.usefixtures("config_driver")
class TestsWithLocators:
    @mark.yes
    def test_option(self):
        self.driver.get(PROPERTIES.qa_url)
        practice_page = PracticePage(self.driver)
        practice_page.select_radio_button_one()

    @mark.no
    def test_option_by_value(self):
        self.driver.get(PROPERTIES.qa_url)
        practice_page = PracticePage(self.driver)
        practice_page.select_radio_button_by_name("Radio2")
        print()

    @mark.any
    def test_hide_show(self):
        self.driver.get(PROPERTIES.qa_url)
        practice_page = PracticePage(self.driver)
        text = "Lorem ipsum"
        practice_page.input_text(text)
        practice_page.hide_text()
        assert not practice_page.is_text_displayed()
        practice_page.show_text()
        assert practice_page.is_text_displayed()
        assert practice_page.get_text() == text
