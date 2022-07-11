"""
1. создать функцию(ии) для  определения погоды по данным(Город).
2. Вынести некоторрые данные в константу(ы).
3. Для запуска функции использовать if __name__ == '__main__': запуск!
4. Создать файл test.py  внутри создать Класс для тестирования функции, с помощью unittest.
"""

import requests

BASE_URL: str = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY: str = 'd82759ebf4a4a5ed987117c4027b9dfa'  # if API_KEY not works, generate yours on website


class Weather:
    """
    Class Return curent waether in City

    used URL:
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
    API_KEY = 'd82759ebf4a4a5ed987117c4027b9dfa'
    complete_url = Weather.BASE_URL + "appid=" + Weather.API_KEY + "&q=" + self.city
    """

    def __init__(self, city_name: str):
        self.city = city_name

    @property
    def _data_getter(self) -> dict | str:
        complete_url: str = BASE_URL + "appid=" + API_KEY + "&q=" + self.city
        response: any = requests.get(complete_url)
        raw_data: dict | str = response.json()
        return raw_data

    @property
    def _data_handler(self) -> str:
        """
        Function take City Name as arg
        Return:
            Weather description: (Like "Broken Clouds")
            Temperature: Deg C
            Pressure: mm Hg
        """
        weather_data: dict = self._data_getter

        main_data: dict = weather_data['main']
        secondary_data: dict = weather_data["weather"]

        current_t: float = main_data['temp']
        current_p: str = main_data["pressure"]

        weather_description: str = secondary_data[0]["description"]

        return f'\n{self.city}\n\n' \
               f'{weather_description.title()}\n' \
               f'Temperature: {str((round(current_t - 273.15)))}C\n' \
               f'Air Pressure: {str(current_p)}mm Hg'

    @property
    def response(self) -> object:
        """Make server_response for 401, 404, 200 cod"""
        try:
            server_response: dict = self._data_getter
        except TypeError:
            return "Use the city Name"
        cod = server_response['cod']
        if cod == 200:
            return self._data_handler
        return server_response['message']


if __name__ == '__main__':
    zp_weather = Weather('Kharkiv')  # 'London'
    print(zp_weather.response)
