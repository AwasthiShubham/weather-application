import requests

class ApiData():
    def __init__(self, api_url):
        self.api_url = api_url

    def get_api_response(self):
        print('API works!')