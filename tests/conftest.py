import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_runtest_setup(item):
    print("Test session start")


def pytest_runtest_teardown(item):
    print("Test session teardown")


@pytest.yield_fixture()
def config_driver(request):
    caps = DesiredCapabilities().EDGE.copy()
    caps['acceptInsecureCerts'] = True
    path = EdgeChromiumDriverManager().install()
    driver = webdriver.Edge(executable_path=path, capabilities=caps)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()
