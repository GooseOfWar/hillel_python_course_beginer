"""
Test for weather_in_city fun
"""

from unittest import TestCase, main

from HW_15.voropaiev_illia_task_1_hw_15 import Weather


class TestWeatherInCity(TestCase):
    #
    def test_city_1(self):
        """Test case: wrong City Name"""
        new_weather1 = Weather('fffddf')
        result = new_weather1.response
        self.assertEqual(result, 'city not found')

    def test_city_2(self):
        """Test case: wrong City Name not str"""
        new_weather2 = Weather(5155)
        result = new_weather2.response
        self.assertEqual(result, 'Use the city Name')

    def test_city_is_true(self):
        """Test case: City name is OK"""
        new_weather = Weather('Kyiv')
        result = new_weather.response
        self.assertIn('Temperature', result)

    def test_wrong_api(self):
        """Test case: wrong API"""

        Weather.API_KEY = 'd8275000000000000000'
        new_weather = Weather('London')
        result = new_weather.response

        self.assertEqual(result, 'Invalid API key.'
                                 ' Please see http://openweathermap.org/faq#error401 for more info.')


if __name__ == '__main__':
    main()
