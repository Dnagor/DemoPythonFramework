import pytest

from sdk.pages.worker import Worker


def pytest_runtest_setup(item):
    print("test session start")


def pytest_runtest_teardown(item):
    print("test session teardown")

@pytest.fixture(scope='function')
def configure_worker():
    worker = Worker("Andriy", 25)

    yield worker

    print(worker.name)