import pytest
import json
from tests.api.api_base import CurrentWeatherAPI
from test_data.data_loader import searched_location_data_list
from api_schema.current_weather_api_schema import CURRENT_WEATHER_SCHEMA
from jsonschema import validate


class TestCurrentWeatherAPI(CurrentWeatherAPI):

    @pytest.mark.parametrize("city_name,country_code", [(location["city"], location["country"])
                                                        for location in searched_location_data_list])
    def test_current_wheather_by_cityname_api(self, city_name, country_code):
        # Execute
        response = self.call_current_weather_by_cityname_api(city_name=city_name)
        # Verify status code
        assert response.status_code == 200
        # Verify response time is less than 3 seconds
        assert response.elapsed.total_seconds() <= 3
        # Verify response body schema as expectation
        validate(instance=json.loads(response.text), schema=CURRENT_WEATHER_SCHEMA)
        print(json.loads(response.text))
        print(type(json.loads(response.text)))

    @pytest.mark.parametrize("city_name", ['london'])
    def test_current_wheather_by_cities_in_circle_api(self, city_name):
        # Execute
        response = self.call_current_weather_by_cities_in_circle_api(q=city_name)
        # Verify status code
        assert response.status_code == 200
