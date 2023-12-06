import pytest

from sdk.pages.worker import Worker
from tests import PROPERTIES
from pytest import mark


@pytest.mark.imagined
class Test_class_one:

    @mark.yes
    def test_yes(self, configure_worker):
        workerFromConfig = configure_worker
        worker = Worker("Andriy", 25)
        assert worker.name == workerFromConfig.name
        workerFromConfig.name = "Oleg"

    @mark.no
    def test_no(self):
        PROPERTIES.browser == "chrome"
        print("test one")

    @mark.any
    def test_any(self):
        PROPERTIES.browser == "chrome"
        print("test one")



