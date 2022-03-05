from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from itertools import product
import os

driver = wd.Firefox()
noisylegrand_URL = "https://payer-fps.noisylegrand.fr/index.jsp?reset"

driver.get(noisylegrand_URL)

L = ['A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
C = ['0','1','2','3','4','5','6','7','8','9']

prod1 = list(map(''.join,[i for i in product(L,repeat=2)]))
prod2 = list(map(''.join,[i for i in product(C,repeat=3)]))
prod4 = list(map(''.join,[i for i in product(prod1,prod2)]))

contravention = []
compteur = 0

for i in range(1,24):

    comb = list(map(''.join,[i for i in product(prod4,prod1[i*23:i*23+23])]))

    for immatriculation in comb:

        plaque = immatriculation[0:2] + '-' + immatriculation[2:5] + '-' + immatriculation[5:7]

        print(f"Plaque en cours : {plaque}") 
        print(f"Plaques testées : {compteur} / 279841000 soit {round(compteur/279841000,10)} %")
        print(f"Plaques avec contravention trouvées : {contravention}")

        compteur += 1

        try:
            checkbox = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((
                    By.XPATH, """//*[@id="checkbox"]""")))
            checkbox.click()
        except:
            pass

        try:
            btn_envoyer = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((
                    By.XPATH, """/html/body/div[1]/form/div[2]/input""")))
            btn_envoyer.click()
        except:
            pass
        
        try:
            space = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((
                    By.XPATH, """//*[@id="immatriculation"]""")))
            space.send_keys(plaque)
        except:
            pass
        
        try:
            btn_valider = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((
                    By.XPATH, """//*[@id="form"]/div[2]/input""")))
            btn_valider.click()
        except:
            pass

        try :
            btn_revenir = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((
                    By.XPATH, """/html/body/div[1]/section/div/form/div/a/input""")))
            btn_revenir.click()
        except :
            contravention.append(plaque)
            noisylegrand_URL = "https://payer-fps.noisylegrand.fr/index.jsp?reset"
        
        os.system("cls")

    print(f"Palier de recherche atteint : {round(100/23*i,2)} %")

print("Fin de la recherche")