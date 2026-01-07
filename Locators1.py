from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
wait=WebDriverWait(driver,10)

#ID & Xpath Locators
# wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms"))).send_keys("Lenovo Thinkpad Carbon Laptop")
# driver.find_element(By.XPATH, '//*[@id="small-search-box-form"]/button').click()
# driver.find_element(By.XPATH,)
# time.sleep(15)

# Link_Text and Partial_Link_Text
driver.find_element(By.LINK_TEXT, "Register").click()
wait.until(EC.title_contains("Register"))
print("Test Passed")
