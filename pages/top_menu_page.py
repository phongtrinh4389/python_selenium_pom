from selenium.webdriver.common.by import By

from pages.weather_search_results_page import SearchResultsPage
from webdriver.driver_method import DriverMethod
from settings.config import settings


class TopMenuPage(DriverMethod):
    # -------------------------- Define page's locators here -------------------------------------
    # ---------------- Friendly Name ---- Locator's Method ----------- Locator String ------------

    txt_top_search_box = (By.CSS_SELECTOR, "#nav-search-form #q")

    btn_top_search_submit = (By.XPATH, "//*[@id='nav-search-form']//input[@type='submit']")

    btn_sign_in = (By.ID, "sign_in")

    lnk_api_menu = (By.LINK_TEXT, "API")

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, path):
        self.open_url(settings['url'] + path)

    def search_weather_from_top_menu(self, search_text):
        self.set_text(self.txt_top_search_box, search_text)
        self.press_enter(self.txt_top_search_box)
        return SearchResultsPage(self.driver)




