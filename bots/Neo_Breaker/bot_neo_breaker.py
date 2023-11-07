from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random as r
import time as t

nb_requêtes = 10
names_team = ["Nicolas Gaudemet",
              "Mathieu Ract",
              "Thomas Cosyn",
              "Alexander Morakhovski",
              "Servane Gouillou",
              "Maurits Reijnen",
              "Stephan Adjarian",
              "Amine Cherif Haouat"]

opts = wd.FirefoxOptions()
opts.set_preference("dom.popup_maximum", nb_requêtes)
driver = wd.Firefox(options=opts)
noisylegrand_URL = "https://websearcher-dev.azurewebsites.net/"

driver.get(noisylegrand_URL)

XPATH_BOUTON_APPROFONDI = """//*[@id="component-4"]/div[2]/label[2]/input"""
XPATH_BOUTON_RAPIDE = """//*[@id="component-4"]/div[2]/label[1]/input"""
XPATH_ZONE_TEXTE = """//*[@id="component-5"]/label/textarea"""
XPATH_BOUTON_QUESTION = """//*[@id="component-6"]"""
XPATH_BOUTON_EFFACER = """//*[@id="component-7"]"""

for i in range(nb_requêtes):

    onglets = driver.window_handles
    driver.switch_to.window(onglets[i])

    BOUTON_APPROFONDI = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((
            By.XPATH, XPATH_BOUTON_APPROFONDI)))

    BOUTON_RAPIDE = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((
            By.XPATH, XPATH_BOUTON_RAPIDE)))

    ZONE_TEXTE = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((
            By.XPATH, XPATH_ZONE_TEXTE)))

    BOUTON_QUESTION = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((
            By.XPATH, XPATH_BOUTON_QUESTION)))

    BOUTON_EFFACER = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((
            By.XPATH, XPATH_BOUTON_EFFACER)))

    BOUTON_APPROFONDI.click()

    name = r.choice(names_team)
    question = f"Qui est {name} ?"

    print(f"Question {i+1}/{nb_requêtes} : {question}")

    ZONE_TEXTE.clear()
    ZONE_TEXTE.send_keys(question)
    BOUTON_QUESTION.click()

    if i+1 != nb_requêtes:
        driver.execute_script(
            "window.open('https://websearcher-dev.azurewebsites.net/', \
                '_blank');"
            )

    t.sleep(1)
