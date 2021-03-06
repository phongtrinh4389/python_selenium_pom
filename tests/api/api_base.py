import requests
from settings.config import settings
from utility.filepath import get_secure_var


class CurrentWeatherAPI:
    CURRENT_WEATHER_BY_CITY_NAME_END_POINT = f"{settings['api_endpoint']}/weather"
    CURRENT_WEATHER_BY_CITY_IN_CIRCLE_END_POINT = f"{settings['api_endpoint']}/find"

    def call_current_weather_by_cityname_api(self, city_name=None, state_code=None, country_code=None):
        search = city_name
        if city_name is None:
            raise Exception("You have to input the city name")
        if state_code is not None:
            search += "," + state_code
        if country_code is not None:
            search += "," + country_code

        return requests.get(self.CURRENT_WEATHER_BY_CITY_NAME_END_POINT,
                            params={'q': search, 'appid': get_secure_var('API_KEY')})

    def call_current_weather_by_cities_in_circle_api(self, q=None, lat=None, lon=None, cnt=30):
        if lat is not None and lon is not None:
            params = {'lat': lat, 'lon': lon, 'cnt': cnt, 'appid': get_secure_var('API_KEY')}
        elif q is not None:
            params = {'q': q, 'appid': get_secure_var('API_KEY'), 'type': 'like'}
        else:
            raise Exception("Please check the params")

        return requests.get(self.CURRENT_WEATHER_BY_CITY_NAME_END_POINT, params=params)

