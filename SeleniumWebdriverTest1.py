from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

#driver = webdriver.Chrome()
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
# git checkout -b test---This command is to create new local branch name "test"
# git checkout main ----this command is to switch from current branch to "main" branch
# git branch ---lists all the branches
# git status ----this command is to check the status of current branch files
# git add file/folder_path (git add . ---this means add all files)
# git commit -m "commit name"----this command is to add new commit name
# git push ---push the current branch from local to remote/origin
# git pull ---pull the current remote branch to local
# git log ---this gives all commit history from the branch
# PS C:\Python and PyCharm\Python-Selenium-test> history
#
#   Id CommandLine
#   -- -----------
#    1 giy
#    2 git
#    3 git branch
#    4 git pull
#    5 git log
#    6 git checkout -b test
#    7 git branch
#    8 git status
#    9 git status
#   10 git add .\SeleniumWebdriverTest1.py
#   11 git status
#   12 git commit -m "Change1"
#   13 git status
#   14 git config --global user.email "araghunath14@gmail.com"
#   15 git commit -m "Change1"
#   16 git ststus
#   17 git status
#   18 git status
#   19 git commit
#   20 git commit -m "Added Git Ignore"
#   21 git status
#   22 git commit -m "Added Git Ignore"
#   23 git add .\.gitignore
#   24 git commit -m "Added Git Ignore"
#   25 git status
#   26 git push
#   27  git push --set-upstream origin test
#   28 git add .
#   29 git commit -m "Test btanch Code Added"
#   30 git status
#   31 git push
#   32 git branch
#   33 git checkout main
#   34 git branch
#   35 git pull
#   36 git status
#   37 git checkout test
#   38 git merge main
#   39 git branch



#test branch added
#https://demo.nopcommerce.com/
#https://opensource-demo.orangehrmlive.com/
#http://www.automationpractice.pl/index.php

