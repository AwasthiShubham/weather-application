import time

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

    def get_temp_celcius(self,city_name):
        time.sleep(5)
        return self.driver.find_element_by_xpath("//div[@title='" + 
            city_name + "']/div[@class='temperatureContainer']/span[@class='tempRedText']").text
