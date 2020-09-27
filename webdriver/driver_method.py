from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


WAIT_ELEMENT_CONDITION_TIMEOUT = 30


class DriverMethod:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait_until_element_present(locator)

    def find_elements(self, locator):
        return self.wait_until_elements_present(locator)

    def find_child_element(self, parent_element, child_locator):
        return parent_element.find_element(*child_locator)

    def wait_until_element_present(self, locator, timeout=WAIT_ELEMENT_CONDITION_TIMEOUT):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(ec.presence_of_element_located(locator))

    def wait_until_elements_present(self, locator, timeout=WAIT_ELEMENT_CONDITION_TIMEOUT):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(ec.presence_of_all_elements_located(locator))

    def wait_until_element_visible(self, locator, timeout=WAIT_ELEMENT_CONDITION_TIMEOUT):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(ec.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait_until_element_present(locator)
        element.click()
        print(f"[Step]: Click on the element {locator}")

    def set_text(self, locator, text):
        element = self.wait_until_element_present(locator)
        element.clear()
        element.send_keys(text)
        print(f"[Step]: Set text [{text} to element {locator}]")

    def get_text(self, locator):
        text = self.wait_until_element_visible(locator).text
        print(f"[Step]: Get text [{text} of element {locator}]")
        return text

    def get_attribute(self, locator, attr):
        attr_value = self.wait_until_element_present(locator).get_attribute(attr)
        print(f"[Step]: Get attribute [{attr}={attr_value} of element {locator}]")
        return attr_value

    def press_enter(self, locator):
        element = self.wait_until_element_present(locator)
        element.send_keys(Keys.ENTER)
        print(f"[Step]: Press Enter on element {locator}]")
