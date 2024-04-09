from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time as t

driver = wd.Firefox()

cemantix_URL = "https://cemantix.herokuapp.com/"
champ_lexical_URL = "https://www.rimessolides.com/motscles.aspx?m=s%C3%A9mantique"

driver.get(cemantix_URL)
popup = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="dialog-close"]""")))
popup.click()
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(champ_lexical_URL)

driver.switch_to.window(driver.window_handles[0])

liste_mots = ["corps", "culture", "manger", "sport", "vision", "réseau", "achat", "maladie", "fermer", "voiture"]

for m in liste_mots:
    guess = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="guess"]""")))
    send = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="guess-btn"]""")))
    guess.send_keys(m)
    send.click()

while True:

    best_mot = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """/html/body/article/table/tbody/tr[3]/td[2]"""))).text
    print(f"best_mot = {best_mot}")

    driver.switch_to.window(driver.window_handles[1])
    recherche = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="TextBox1"]""")))

    recherche.clear()
    recherche.send_keys(best_mot)
    recherche.send_keys(Keys.RETURN)

    try:
        mot_du_champ_lexical = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, """/html/body/form/div[4]/div/div[1]/div[2]/div/main/div/span[1]/a"""))).text
    except:
        mot_du_champ_lexical = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, """/html/body/form/div[4]/div/div[1]/div[2]/div/main/div/div[2]/a"""))).text

    print(f"mot_du_champ_lexical = {mot_du_champ_lexical}")

    driver.switch_to.window(driver.window_handles[0])

    guess.send_keys(mot_du_champ_lexical)
    send.click()
    guess.send_keys("mot")
    send.click()

    t.sleep(2)
