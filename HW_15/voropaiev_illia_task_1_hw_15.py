"""
1. создать функцию(ии) для  определения погоды по данным(Город).
2. Вынести некоторрые данные в константу(ы).
3. Для запуска функции использовать if __name__ == '__main__': запуск!
4. Создать файл test.py  внутри создать Класс для тестирования функции, с помощью unittest.

import requests

base_url = 'http://api.openweathermap.org/data/2.5/weather?'

city_name = input('please fill up your city')

API_KEY = 'd82759ebf4a4a5ed987117c4027b9dfa' # if API_KEY not works, generate yours on website

complete_url = base_url + "appid=" + API_KEY + "&q=" + city_name
response = requests.get(complete_url)
r_data = response.json()
if r_data["cod"] != "404":
    y = r_data['main']
    current_t = y['temp']
    current_p = y["pressure"]
    z = r_data["weather"]
    weather_description = z[0]["description"]
    print(str((round(current_t - 273.15))), str(current_p))
else:
    print('city not found')
"""

import requests


class Weather:
    """
    Class Return curent waether in City

    used URL:
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
    API_KEY = 'd82759ebf4a4a5ed987117c4027b9dfa'
    complete_url = Weather.BASE_URL + "appid=" + Weather.API_KEY + "&q=" + self.city
    """

    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
    API_KEY = 'd82759ebf4a4a5ed987117c4027b9dfa'  # if API_KEY not works, generate yours on website

    def __init__(self, sity_name):
        self.city = sity_name

    @property
    def _data_getter(self) -> dict or str:
        complete_url = Weather.BASE_URL + "appid=" + Weather.API_KEY + "&q=" + self.city
        response = requests.get(complete_url)
        raw_data = response.json()
        return raw_data

    def _data_hendler(self):
        """
        Function take City Name as arg
        Return:
            Weather description: (Like "Broken Clouds")
            Temperature: Deg C
            Pressure: mm Hg
        """
        weather_data: dict = self._data_getter

        main_data = weather_data['main']
        secondary_data = weather_data["weather"]

        current_t = main_data['temp']
        current_p = main_data["pressure"]

        weather_description: str = secondary_data[0]["description"]

        return f'\n{self.city}\n\n' \
               f'{weather_description.title()}\n' \
               f'Temperature: {str((round(current_t - 273.15)))}C\n' \
               f'Air Pressure: {str(current_p)}mm Hg'

    @property
    def response(self):
        """Make server_response for 401, 404, 200 cod"""

        try:
            server_response: dict = self._data_getter
        except TypeError:
            return "Use the city Name"
        cod = server_response['cod']
        # Это не работает так как дикт пытается иницыалироваться в любом случае. Что с этим делать?
        # response_variant = {200: self._data_hendler,
        #                     401: server_response['message'],
        #                     '404': server_response['message']}
        # result = response_variant[cod]
        # return result

        if cod == 200:
            return self._data_hendler()
        response_variant = {401: server_response['message'],
                            '404': server_response['message']}
        result = response_variant[cod]
        return result

if __name__ == '__main__':
    zp_weather = Weather('fff')  # 'London'
    print(zp_weather.response)
