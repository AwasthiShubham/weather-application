import unittest
from config.testconfig import TestConfig

class TestWeatherCompare(unittest.TestCase,TestConfig):
    tc = TestConfig()

    def test_ui_temp(self):
        self.tc.load_application()
        self.tc._get_app_data().get_weather_page()
        self.assertTrue(
            self.tc._get_app_data().is_city_displayed("Pune") 
            and 
            self.tc._get_app_data().is_weather_details_displayed("Pune")
            )
        temp_ui = self.tc._get_app_data().get_temp_celcius("Pune")
        self.tc.close_browser()

    def test_api_temp(self):
        temp_api = self.tc._get_api_data().get_api_response("Pune")
        self.assertEqual(temp_api['cod'],200)
        self.assertEqual(temp_api['name'],'Pune')


if __name__ == "__main__":
    unittest.main()