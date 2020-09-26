from selenium.webdriver.common.by import By
from webdriver.driver_method import DriverMethod
from unidecode import unidecode


class SearchResultsPage(DriverMethod):
    # -------------------------- Define page's locators here -------------------------------------
    # ---------------- Friendly Name ---- Locator's Method ----------- Locator String ------------

    txt_search_box = (By.ID, "search_str")

    btn_search_submit = (By.XPATH, "//*[@id='searchform']//input[@type='submit']")

    # ----------- The locators for the searched weather results -------------
    tbl_searched_not_found = (By.ID, "forecast_list_ul")
    # The parent results table
    tbl_searched_results = (By.XPATH, "//*[@id='forecast_list_ul']//tr")
    td_searched_location_name = (By.XPATH, "//td[2]/b[1]")
    td_searched_weather_description = (By.XPATH, "//td[2]/b[2]")
    td_searched_weather_details = (By.XPATH, "//td[2]/p[1]")
    td_searched_geo_coords = (By.XPATH, "//td[2]/p[2]")

    def __init__(self, driver):
        super().__init__(driver)

    def get_searched_results_list(self):
        results = []
        result_elements = self.find_elements(self.tbl_searched_results)
        for result_element in result_elements:
            results.append({
                "city": unidecode(self.find_child_element(result_element, self.td_searched_location_name).
                                  text.split(',')[0]).replace(' ', ''),
                "country": self.find_child_element(result_element, self.td_searched_location_name).text.split(',')[1],
                "weather_description": self.find_child_element(result_element,
                                                               self.td_searched_weather_description).text,
                "weather_details": self.find_child_element(result_element,
                                                           self.td_searched_weather_details).text,
                "geo_coords": self.find_child_element(result_element,
                                                      self.td_searched_geo_coords).text,
            })

        return results

    def get_not_found_message(self):
        return self.get_text(self.tbl_searched_not_found)