import time
from selenium.webdriver.remote.webelement import WebElement

class ApplicationData():
    def __init__(self, driver):
        self.driver = driver
    
    def get_weather_page(self):
        self.driver.find_element_by_xpath("//div[@class='topnav_extra']/a[@id='h_sub_menu']").click()
        self.driver.find_element_by_xpath("//div[@class='topnav_cont']/a[text()='WEATHER']").click()

    def is_city_displayed(self,city_name):
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@class='searchContainer']/input[@id='searchBox']").send_keys(city_name)
        self.driver.find_element_by_xpath("//div[@class='messages']//input[@id='" + city_name + "']").click()
        return self.driver.find_element_by_xpath("//div[@class='outerContainer']/div[text()='" + city_name +"']").is_displayed()

    def is_weather_details_displayed(self,city_name):
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@class='outerContainer']/div[text()='" + city_name +"']").click()
        time.sleep(5)
        return city_name in self.driver.find_element_by_xpath("//div[contains(@class,'leaflet-popup')]//span[2]").text

    def get_temp_celcius(self,city_name):
        time.sleep(5)
        return self.driver.find_element_by_xpath("//div[@title='" + 
            city_name + "']/div[@class='temperatureContainer']/span[@class='tempRedText']").text
