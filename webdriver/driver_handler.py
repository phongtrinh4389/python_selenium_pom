from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from settings.config import settings
from utility.filepath import get_secure_var
import os


def cloud_driver():
    if os.getenv('browser') is None:
        browser = str(settings['cloud']['browser']).lower()
    else:
        browser = os.getenv('browser')

    desired_cap = {
        'os_version': settings['cloud']['os_version'],
        'resolution': settings['cloud']['resolution'],
        'browser': browser,
        'browser_version': settings['cloud']['browser_version'],
        'os': settings['cloud']['os']
    }
    command_executor = settings['cloud']['cloud_host'].format(get_secure_var('BROWSERSTACK_USERNAME'),
                                                              get_secure_var('BROWSERSTACK_ACCESS_KEY'))
    # Instantiate an instance of Remote WebDriver with the desired capabilities.
    driver = webdriver.Remote(desired_capabilities=desired_cap, command_executor=command_executor)
    return driver


def local_driver():
    if os.getenv('browser') is None:
        browser = str(settings['local']['browser']).lower()
    else:
        browser = os.getenv('browser')

    if browser.lower() == "firefox":
        return webdriver.Firefox(GeckoDriverManager().install())
    elif browser.lower() == "chrome":
        return webdriver.Chrome(ChromeDriverManager().install())
    else:
        raise Exception(f"Browser [{browser}] has not been implemented")


def remote_driver():
    if os.getenv('browser') is None:
        browser = str(settings['remote']['browser']).lower()
    else:
        browser = os.getenv('browser')

    if browser.lower() == "firefox":
        return webdriver.Remote(command_executor=settings['remote']['remote_url'],
                                desired_capabilities=DesiredCapabilities.FIREFOX)
    elif browser.lower() == "chrome":
        return webdriver.Remote(command_executor=settings['remote']['remote_url'],
                                desired_capabilities=DesiredCapabilities.CHROME)
    else:
        raise Exception(f"Browser [{browser}] has not been implemented")


class DriverHandler:
    __driver = None

    def __init__(self):
        if os.environ.get('running_type') is None:
            running_type = str(settings['running_type']).lower()
        else:
            running_type = os.getenv('running_type')

        if running_type == 'remote':
            self.__driver = remote_driver()
        elif running_type == 'cloud':
            self.__driver = cloud_driver()
        else:
            self.__driver = local_driver()

    def get_driver(self):
        self.__driver.maximize_window()
        return self.__driver
