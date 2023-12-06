import pytest

from tests import PROPERTIES
from pytest import mark


@pytest.mark.not_imagined
class test_class_one:

    @mark.yes
    def test_yes(self):
        PROPERTIES.browser == "chrome"
        PROPERTIES.anyParameter = "aaa"
        print("test one")

    @mark.no
    def test_no(self):
        PROPERTIES.browser == "chrome"
        print("test one")

    @mark.any
    def test_any(self):
        PROPERTIES.browser == "chrome"
        print("test one")



