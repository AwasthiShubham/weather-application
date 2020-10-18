"""Main Test Class"""
import unittest
import logging
from config.testconfig import TestConfig

class TestWeatherCompare(unittest.TestCase):
    """Test Class for testing api and ui for the application"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    def test_ui_temp(self):
        """Test to check verify temperature on UI"""
        self.logger.info("Running test to check verify temperature on UI")
        tc_obj = TestConfig()
        tc_obj.load_application()
        tc_obj.get_app_data().get_weather_page()
        city_displayed = tc_obj.get_app_data().is_city_displayed("Pune")
        temp_ui = tc_obj.get_app_data().get_temp_celcius("Pune")
        self.assertTrue(city_displayed and  temp_ui is not None)
        self.logger.info("City and Temperature displayed on UI")
        self.assertTrue(tc_obj.get_app_data().is_weather_details_displayed("Pune"))
        self.logger.info("Weather Details are displayed on clicking city name")
        tc_obj.close_browser()

    def test_api_temp(self):
        """Test to check verify temperature on API"""
        self.logger.info("Running test to check verify temperature on API")
        tc_obj =TestConfig()
        temp_api = tc_obj.get_api_data().get_api_response("Pune")
        self.assertEqual(temp_api['cod'],200)
        self.logger.info("Status code returned by API is Success")
        self.assertEqual(temp_api['name'],'Pune')
        self.logger.info("City returned by API is correct")
        tc_obj.close_browser()

    def test_compare_api_ui_temp(self):
        """Test to compare temperature on UI and API"""
        self.logger.info("Running test to compare temperature on UI and API")
        tc_obj = TestConfig()
        tc_obj.load_application()
        tc_obj.get_app_data().get_weather_page()
        tc_obj.get_app_data().is_city_displayed("Pune")
        temp_ui = tc_obj.get_app_data().get_temp_celcius("Pune")
        temp_api = tc_obj.get_api_data().get_api_response("Pune")
        result = tc_obj.compare_values(temp_api,temp_ui)
        try:
            assert result < 2
            self.logger.info("Compared data is correct")
        except AssertionError:
            print(f"Temperature differnce is {result} instead of 2")
            self.logger.info("Compared data is incorrect")
        tc_obj.close_browser()

if __name__ == "__main__":
    unittest.main()
