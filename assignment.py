# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca/")
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
# search_bar = driver.find_element("id","twotabsearchtextbox")
# search_bar.send_keys("laptop")
Prime_Day_Deals= driver.find_element("id","nav-primeday")
Prime_Day_Deals.click()

time.sleep(3)
# Verifying that the prime page has loaded
assert "Amazon.ca | Prime Day 2023" in driver.title

Sports_and_Outdoor_Link= driver.find_element("xpath","/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[8]")
Sports_and_Outdoor_Link.click()
time.sleep(3)



School_supplies= driver.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/section/div/div/div[2]/div[2]/div/ol/li[4]/a/div[1]/img")
School_supplies.click()
time.sleep(3)

Crayola_paints= driver.find_element("xpath","/html/body/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/section/div[4]/figure/div/a/div[2]/div/div[1]/div[1]/span")
Crayola_paints.click()

time.sleep(3)

set_delivery_option= driver.find_element("id","contextualIngressPtLabel_deliveryShortLine")
set_delivery_option.click()
time.sleep(4)

sign_in_option= driver.find_element("xpath","/html/body/div[9]/div/div/div/div/div[2]/div[1]/span/span/input")
sign_in_option.click()

time.sleep(4)

assert "Amazon Sign In" in driver.title

#  # Closing the webdriver
driver.close()