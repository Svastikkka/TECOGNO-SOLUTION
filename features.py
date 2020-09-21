from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("/Users/manshusharma/Downloads/chromedriver")
driver.get("https://www.tripadvisor.com/Hotels-g304551-New_Delhi_National_Capital_Territory_of_Delhi-Hotels.html")

elem1 = driver.find_elements_by_xpath("//*[contains(@class, 'prw_rup prw_common_hotel_icons_list linespace is-shown-at-tablet')]")

for li in elem1:
    for j in li.find_elements_by_class_name("text"):
        print(j.get_attribute("innerHTML"),end=" ")
    print()
driver.close()
