from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import gensim.downloader as api

model = api.load("fasttext-wiki-news-subwords-300")

global liste_mots
liste_mots = ["corps", "culture", "manger", "sport", "vision", "réseau", "achat", "maladie", "fermer", "voiture"]


def mots_similaires(mots, liste_mots, topn=10):
    mots_similaires = []
    for mot in mots:
        if mot in model.key_to_index:
            similaires = model.most_similar(mot, topn=topn)
            mots_similaires.append([sim for sim in similaires if sim[0] not in liste_mots])
        else:
            mots_similaires.append([(mot, 1.0)])  # Ajouter le mot lui-même s'il n'est pas trouvé
    return mots_similaires


driver = wd.Firefox()

pimiento_URL = "https://pimiento.janvier.tv/fr"

driver.get(pimiento_URL)
popup = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="rules-close"]""")))
popup.click()

for m in liste_mots:
    guess = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="guess_plat"]""")))
    send = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="guess-btn_plat"]""")))
    guess.send_keys(m)
    send.click()

while True:

    best_mot_1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """/html/body/div[5]/table/tbody/tr[2]/td[2]"""))).text
    best_mot_2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """/html/body/div[5]/table/tbody/tr[2]/td[2]"""))).text
    best_mot_3 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """/html/body/div[5]/table/tbody/tr[2]/td[2]"""))).text

    liste_word = mots_similaires([best_mot_1, best_mot_2, best_mot_3], liste_mots)

    for m in liste_word:
        print(liste_word)
        liste_mots.append(m)
        guess = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="guess_plat"]""")))
        send = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="guess-btn_plat"]""")))
        guess.send_keys(m)
        send.click()
