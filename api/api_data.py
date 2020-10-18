"""Module to perform action on API"""
import json
import requests


class ApiData():
    """Class to fetch data from API"""
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def get_api_response(self,city_nmae):
        """Function to get data from API"""
        url = self.api_url + "&appid=" + self.api_key + "&q="+ city_nmae +"&units=metric"
        response = requests.request("GET",url)
        json_data = json.loads(response.text)
        return json_data
