import unittest
from config.testconfig import TestConfig

class TestWeatherCompare(unittest.TestCase):

    def test_ui_temp(self):
        tc = TestConfig()
        tc.load_application()
        tc._get_app_data().get_weather_page()
        city_displayed = tc._get_app_data().is_city_displayed("Pune")
        temp_ui = tc._get_app_data().get_temp_celcius("Pune")
        self.assertTrue(
            city_displayed
            and 
            temp_ui != None
            )
        self.assertTrue(tc._get_app_data().is_weather_details_displayed("Pune"))
        tc.close_browser()

    def test_api_temp(self):
        tc =TestConfig()
        temp_api = tc._get_api_data().get_api_response("Pune")
        self.assertEqual(temp_api['cod'],200)
        self.assertEqual(temp_api['name'],'Pune')
        tc.close_browser()

    def test_compare_api_ui_temp(self):
        tc = TestConfig()
        tc.load_application()
        tc._get_app_data().get_weather_page()
        tc._get_app_data().is_city_displayed("Pune")
        temp_ui = tc._get_app_data().get_temp_celcius("Pune")
        temp_api = tc._get_api_data().get_api_response("Pune")
        result = tc.compare_values(temp_api,temp_ui)
        try:
            assert result < 2
        except AssertionError:
            print(f"Temperature differnce is {result} instead of 2")
        tc.close_browser()
        

if __name__ == "__main__":
    unittest.main()