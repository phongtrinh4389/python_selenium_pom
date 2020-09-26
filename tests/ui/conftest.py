import os
from datetime import datetime
import pytest
from selenium import webdriver
from webdriver.driver_handler import DriverHandler


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None)
    # Add more arguments here


@pytest.fixture(autouse=True, scope="session")
def setup_01_load_pytest_argument(pytestconfig):
    if pytestconfig.getoption("browser") is not None:
        os.environ["browser"] = pytestconfig.getoption("browser")

    yield

    if "browser" in os.environ.keys():
        os.environ.pop("browser")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # to remove environment section
    config._metadata = None

    if not os.path.exists('reports'):
        os.makedirs('reports')

    config.option.htmlpath = 'reports/' + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"


@pytest.fixture(scope="function")
def driver_init(request):
    driver = DriverHandler().get_driver()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.usefixtures("driver_init")
class BaseTest(object):
    pass
