from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

wait = WebDriverWait(driver, 15)

wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

# Verify login by title or dashboard element
wait.until(EC.title_contains("OrangeHRM"))

print("Login Test Passed")

driver.quit()


# code change

#https://demo.nopcommerce.com/
#https://opensource-demo.orangehrmlive.com/
#http://www.automationpractice.pl/index.php

