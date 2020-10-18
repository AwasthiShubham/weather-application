"""Module to fetch data from UI"""
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class ApplicationData():
    """Class to fetch data from UI"""
    def __init__(self, driver):
        self.driver = driver

    def get_weather_page(self):
        """Function to get to weather page"""
        menu_expand_icon = self.driver.find_element_by_xpath("//div[@class='topnav_extra']/a[@id='h_sub_menu']")
        menu_expand_icon.click()
        weather_icon = self.driver.find_element_by_xpath("//div[@class='topnav_cont']/a[text()='WEATHER']")
        weather_icon.click()

    def is_city_displayed(self,city_name):
        """Function to check if the city is displayed on the page"""
        self.wait_for_element_exist("//div[@class='searchContainer']/input[@id='searchBox']")
        input_city = self.driver.find_element_by_xpath("//div[@class='searchContainer']/input[@id='searchBox']")
        input_city.click()
        input_city.clear()
        input_city.send_keys(city_name)
        checkbox_city = self.driver.find_element_by_xpath("//div[@class='messages']//input[@id='" + city_name + "']")
        checkbox_city.click()
        self.wait_for_element_exist("//div[@class='outerContainer']/div[text()='" + city_name +"']")
        city_on_map = self.driver.find_element_by_xpath("//div[@class='outerContainer']/div[text()='" + city_name +"']")
        return city_on_map.is_displayed()

    def is_weather_details_displayed(self,city_name):
        """Function to check if the weather details are displayed on the page"""
        self.wait_for_element_exist("//div[@class='outerContainer']/div[text()='" + city_name +"']")
        city_on_map = self.driver.find_element_by_xpath("//div[@class='outerContainer']/div[text()='" + city_name +"']")
        city_on_map.click()
        self.wait_for_element_exist("//div[contains(@class,'leaflet-popup')]//span[2]")
        pop_up_city = self.driver.find_element_by_xpath("//div[contains(@class,'leaflet-popup')]//span[2]")
        pop_up_city_name = pop_up_city.text
        return city_name in pop_up_city_name

    def get_temp_celcius(self,city_name):
        """Function to get temperature in celcius unit from the page"""
        self.wait_for_element_exist("//div[@title='" + city_name + "']/div[@class='temperatureContainer']/span[@class='tempRedText']")
        temp_celcius = self.driver.find_element_by_xpath("//div[@title='" + city_name + "']/div[@class='temperatureContainer']/span[@class='tempRedText']")
        return temp_celcius.text

    def wait_for_element_exist(self,locator):
        """Wais for element to be present"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,locator)))     
