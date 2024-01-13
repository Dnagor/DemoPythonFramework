from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

_DRIVER = None


def get_driver(browser: str = "edge"):
    global _DRIVER
    if not _DRIVER:
        if browser == "edge" or browser is None:
            caps = DesiredCapabilities().EDGE.copy()
            caps['acceptInsecureCerts'] = True
            path = EdgeChromiumDriverManager().install()
            _DRIVER = webdriver.Edge(executable_path=path, capabilities=caps)
            _DRIVER.implicitly_wait(10)
        elif browser == "firefox":
            _DRIVER = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            _DRIVER.maximize_window()
    return _DRIVER


def close_driver():
    global _DRIVER
    if _DRIVER:
        _DRIVER.quit()
        _DRIVER = None
