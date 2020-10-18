"""Module to call config for weater application test"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from ui.application_data import ApplicationData
from api.api_data import ApiData

class TestConfig():
    """Class to invoke configurations for the waeather application"""
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.app_url = 'https://www.ndtv.com/'
        self.api_url = 'http://api.openweathermap.org/data/2.5/weather?'
        self.api_key = '7fe67bf08c80ded756e598d6f8fedaea'

    def get_driver(self):
        """Function to call driver object"""
        return self.driver

    def get_application_url(self):
        """Returns url for the application ui"""
        return self.app_url

    def get_app_data(self):
        """Returns object to fetch application data from ui"""
        app_data = ApplicationData(self.driver)
        return app_data

    def get_apiurl(self):
        """Returns url for application API"""
        return self.api_url

    def get_api_data(self):
        """Returns object to fetch data from API"""
        api_data = ApiData(self.get_apiurl(),self.get_api_key())
        return api_data

    def get_api_key(self):
        """Returns key for API validation"""
        return self.api_key

    def load_application(self):
        """Loads application when called"""
        self.driver.get(self.get_application_url())
        self.driver.maximize_window()

    def close_browser(self):
        """Closes browser when called"""
        self.driver.close()

    def compare_values(self,api_value, ui_value):
        """Compares objects to return differntial value"""
        api_val = int(float((api_value['main']['temp'])))
        ui_val = int(ui_value[:-1])
        diff = abs(api_val-ui_val)
        return diff
