import pytest
from pytest import mark

from sdk.pages.practice_page import PracticePage
from tests import PROPERTIES


@pytest.mark.usefixtures("config_driver")
class TestsWithSwitchTo:
    @mark.yes
    def test_switch_to_alert(self):
        user = "User"
        self.driver.get(PROPERTIES.qa_url)
        practice_page = PracticePage(self.driver)
        practice_page.input_name(user)
        practice_page.click_alert_button()
        alert_text = practice_page.get_text_from_alert()
        assert alert_text == f"Hello {user}, share this practice page and share your knowledge"

    @mark.no
    def test_swithch_between_tabs(self):
        self.driver.get(PROPERTIES.qa_url)

    @mark.any
    def test_switch(self):
        self.driver.get(PROPERTIES.qa_url)
