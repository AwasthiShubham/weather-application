import unittest
from config.testconfig import TestConfig

class TestWeatherCompare(unittest.TestCase,TestConfig):
    tc = TestConfig()

    def setUp(self):
        self.tc.load_application()


    def test_ui_temp(self):
        self.tc._get_app_data().get_weather_page()
        self.assertTrue(self.tc._get_app_data().is_city_displayed("Pune"))
        temp_ui = self.tc._get_app_data().get_temp_celcius("Pune")
        print(temp_ui)
        self.tc._get_api_data().get_api_response()


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()