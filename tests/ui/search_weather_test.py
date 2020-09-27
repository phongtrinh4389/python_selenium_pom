import re
import pytest

from tests.ui.conftest import BaseTest
from pages.top_menu_page import TopMenuPage
from test_data.data_loader import searched_location_data_list


class TestSearchWeatherSuccess(BaseTest):

    @pytest.mark.parametrize("city,country", [(location["city"], location["country"])
                                              for location in searched_location_data_list])
    def test_searching_weather_success(self, city, country):
        # ---------------- Open the page then search weather ----------------
        top_menu_page = TopMenuPage(self.driver)
        top_menu_page.open_page('/')
        search_result_page = top_menu_page.search_weather_from_top_menu(f"{city}, {country}")
        results = search_result_page.get_searched_results_list()

        # ---------------- Verify the searched results -----------------------
        for result in results:
            # Verify the returned location
            assert city.lower() in result["city"].lower(), f"The returned city is incorrect, expect [{city}] " \
                                                           f"but found [{result['city']}] "

            assert country.lower() in result["country"].lower(), f"The returned country is incorrect, " \
                                                                 f"expect [{country}] but found [{result['country']}] "
            # Verify the weather detail format
            pattern = r"[-+]?\d*\.\d+||\d+°С temperature from [-+]?\d*\.\d+||\d+ to [-+]?\d*\.\d+||\d+ °С, " \
                      r"wind [-+]?\d*\.\d+||\d+ m\/s\. clouds [-+]?\d*\.\d+||\d+ %, [-+]?\d*\.\d+||\d+ hpa"
            weather_detail = result['weather_details']
            assert re.match(pattern, weather_detail), "The Weather detail format is not correct"

            # Verify the coord format
            pattern = r"Geo coords \[[-+]?\d*\.\d+||\d+, [-+]?\d*\.\d+||\d+\]"
            coords = result['geo_coords']
            assert re.match(pattern, coords), "The Coords format is not correct"

    @pytest.mark.parametrize("city,country", [('sdfsdfdf', 'eff')])
    def test_searching_weather_not_found(self, city, country):
        # ---------------- Open the page then search weather ----------------
        top_menu_page = TopMenuPage(self.driver)
        top_menu_page.open_page('/')
        search_result_page = top_menu_page.search_weather_from_top_menu(f"{city}, {country}")
        message = search_result_page.get_not_found_message()
        assert 'Not found' in message
