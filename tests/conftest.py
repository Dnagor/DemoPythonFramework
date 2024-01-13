import logging as log
import os
from datetime import datetime

import pytest

import sdk.utils.driver_manager as dm


def pytest_runtest_setup(item):
    log.info(f"====={item.name}=====")


def pytest_runtest_teardown(item):
    log.info(f"====={item.name}=====")


@pytest.yield_fixture(scope="function")
def config_driver(request, browser):
    driver = dm.get_driver(browser)
    request.cls.driver = driver
    yield
    dm.close_driver()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.failed:
        now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        base_path = os.path.dirname(os.path.dirname(__file__))

        screen_path = os.path.abspath("{}/{}/{}_{}.png".format(base_path,
                                                               "logs\\screenshots",
                                                               item.name.replace(" ", "_"),
                                                               str(now)))
        driver = dm.get_driver()
        try:
            driver.save_screenshot(screen_path)
        except Exception as msg:
            log.warning(f"Could not make a screenshot: {msg}")
