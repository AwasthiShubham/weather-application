import unittest
from config.testconfig import TestConfig

class TestWeatherCompare(unittest.TestCase):
    tc = TestConfig()

    def setUp(self):
        self.tc.load_application()


    def test_something(self):
        self.tc._get_app_data().get_weather_page()
        self.tc._get_api_data().get_api_response()


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()