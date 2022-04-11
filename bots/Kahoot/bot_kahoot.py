import re
from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time as t

### Ajouter un seul joueur

# game_PIN = "3320776"
# name = "mathieu4"
# 
# driver = wd.Firefox()
# kahoot_URL = "https://kahoot.it/"
# 
# driver.get(kahoot_URL) # ouvre instagram
# 
# PIN = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="game-input"]"""))) # défini le bouton fermer
# PIN.send_keys(game_PIN)
# PIN.send_keys(Keys.RETURN)
# 
# NICKNAME = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="nickname"]""")))
# NICKNAME.send_keys(name)
# NICKNAME.send_keys(Keys.RETURN)

### Ajouter n Joueurs

game_PIN = "1305359"
texte = "Samuel est une petite salope" # 7 mots maximum

driver = wd.Firefox()
kahoot_URL = "https://kahoot.it/"

list = texte.split(" ")
list_name = [list[-i-1] for i in range(len(list))]

for i in range(len(list_name)):

    enter = False
    while enter == False:
        try :
            driver.get(kahoot_URL)
            
            PIN = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="game-input"]"""))) # défini le bouton fermer
            PIN.send_keys(game_PIN)
            PIN.send_keys(Keys.RETURN)
            
            NICKNAME = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="nickname"]""")))
            NICKNAME.send_keys(list_name[i])
            NICKNAME.send_keys(Keys.RETURN)
            
            driver.execute_script("window.open();") # ouvre une nouvelle fenetre
            window_after = driver.window_handles[i+1]
            driver.switch_to.window(window_after)
            enter = True
        except :
            t.sleep(1)
        