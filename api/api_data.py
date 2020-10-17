import requests
import json

class ApiData():
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def get_api_response(self,city_name):
        url = self.api_url + "&appid=" + self.api_key + "&q=pune&units=metric"
        response = requests.request("GET",url)
        json_data = json.loads(response.text)
        return json_data["main"]["temp"]