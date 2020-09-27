import os
from datetime import datetime
import pytest
from webdriver.driver_handler import DriverHandler


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None)
    parser.addoption("--running_type", action="store", default=None)


@pytest.fixture(autouse=True, scope="session")
def load_pytest_arguments(pytestconfig):
    if pytestconfig.getoption("browser") is not None:
        os.environ["browser"] = pytestconfig.getoption("browser")

    if pytestconfig.getoption("running_type") is not None:
        os.environ["running_type"] = pytestconfig.getoption("running_type")

    yield

    if "browser" in os.environ.keys():
        os.environ.pop("browser")

    if "running_type" in os.environ.keys():
        os.environ.pop("running_type")


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
