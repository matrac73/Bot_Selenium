from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from data_partners import personnes
import random as r
import time as t
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv(key="email")
PASSWORD = os.getenv(key="password")

nb_requêtes = 5

opts = wd.FirefoxOptions()
opts.set_preference(name="dom.popup_maximum", value=nb_requêtes)
driver = wd.Firefox(options=opts)
URL_copilot = "https://www.office.com/chat?auth=2"

driver.get(url=URL_copilot)

EMAIL_ZONE_XPATH = """//*[@id="i0116"]"""
PASSWORD_ZONE_XPATH = """//*[@id="i0118"]"""
YES_XPATH = """//*[@id="idSIButton9"]"""
ZONE_TEXTE_XPATH = """//*[@id="m365-chat-editor-target-element"]"""
PROMPT_LIBRARY_XPATH = """/html/body/div[1]/div/div/div/div[1]/div/div/\
    div/div[1]/div[3]/div/button"""

EMAIL_ZONE = WebDriverWait(driver=driver, timeout=60).until(
        method=EC.visibility_of_element_located(locator=(
            By.XPATH, EMAIL_ZONE_XPATH)))
EMAIL_ZONE.send_keys(EMAIL)
EMAIL_ZONE.send_keys(Keys.RETURN)

PASSWORD_ZONE = WebDriverWait(driver=driver, timeout=60).until(
        method=EC.visibility_of_element_located(locator=(
            By.XPATH, PASSWORD_ZONE_XPATH)))
PASSWORD_ZONE.send_keys(PASSWORD)
PASSWORD_ZONE.send_keys(Keys.RETURN)

for remaining_time in range(10, 0, -1):
    countdown_str = f"Temps restant : {remaining_time} secondes"
    clear_line = " " * len(countdown_str)
    print(countdown_str, end="\r")
    t.sleep(1)
    print(clear_line, end="\r")

print("Le timer est terminé!")

YES = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((
            By.XPATH, YES_XPATH)))
YES.click()

for i in range(nb_requêtes):

    driver.execute_script(script="window.scrollTo(0, 0);")

    onglets = driver.window_handles
    driver.switch_to.window(window_name=onglets[i])

    #  N'arrive pas détecter la zone de texte
    ZONE_TEXTE = WebDriverWait(driver=driver, timeout=60).until(
        method=EC.visibility_of_element_located(locator=(
            By.XPATH, ZONE_TEXTE_XPATH)))

    name = r.choice(seq=personnes)
    question = f"What's the latest from {name}, \
        organized by emails, chats, and files?"

    print(f"Question {i+1}/{nb_requêtes} : {question}")

    ZONE_TEXTE.clear()
    ZONE_TEXTE.send_keys(question)
    ZONE_TEXTE.send_keys(Keys.RETURN)

    if i+1 != nb_requêtes:
        driver.execute_script(
            "window.open('https://websearcher-dev.azurewebsites.net/', \
                '_blank');"
            )
    else:
        driver.execute_script("window.scrollTo(0, 0);")

    t.sleep(1)
