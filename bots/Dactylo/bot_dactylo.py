import re
from selenium import webdriver as wd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time as t

### Page + login

driver = wd.Firefox() # défini le browser firefox par défaut
insta_URL = "https://10fastfingers.com/login"

driver.get(insta_URL) # ouvre instagram
driver.maximize_window() # plein écran

pop = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="CybotCookiebotDialogBodyLevelButtonAccept"]""")))
pop.click()

email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="UserEmail"]""")))
email.send_keys("mathieu.ract@gmail.com")

mdp = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="UserPassword"]""")))
mdp.send_keys("verrenss")

button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="login-form-submit"]""")))
button.click()

pop = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """/html/body/div[9]/div/button""")))
pop.click()

### Ecriture

w = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="inputfield"]""")))

for i in range (1,400) :
    r = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div[4]/div/div[1]/div[7]/div[1]/div/span["+str(i)+"]")))
    w.send_keys(r.text)
    w.send_keys(Keys.SPACE)