from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from ui.application_data import ApplicationData
from api.api_data import ApiData

class TestConfig():

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def _get_driver(self):
        return self.driver

    def _get_application_url(self):
        app_url = 'https://www.ndtv.com/'
        return app_url

    def _get_app_data(self):
        app_data = ApplicationData(self.driver)
        return app_data

    def _get_apiurl(self):
        api_url = 'http://api.openweathermap.org/data/2.5/weather?'
        return api_url

    def _get_api_data(self):
        api_data = ApiData(self._get_apiurl(),self._get_api_key())
        return api_data

    def _get_api_key(self):
        api_key = '7fe67bf08c80ded756e598d6f8fedaea'
        return api_key

    def load_application(self):
        self.driver.get(self._get_application_url())
        self.driver.maximize_window()

    def close_browser(self):
        self.driver.close()