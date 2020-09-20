from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# import the webdriver, chrome driver is recommended
driver = webdriver.Chrome("/Users/manshusharma/Downloads/chromedriver")

# insert the tripadvisor's website of one attraction _1shPZD63
driver.get("https://www.tripadvisor.com/Hotels-g304551-New_Delhi_National_Capital_Territory_of_Delhi-Hotels.html")

features=driver.find_elements_by_class_name("text")

p=[]
for i in features :
    if (i.get_attribute("innerHTML") != "null"):
        p.append(i.get_attribute("innerHTML"))

print(p)
driver.close()
