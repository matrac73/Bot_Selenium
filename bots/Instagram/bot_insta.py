### A SAVOIR AVANT DE LANCER LE PGM

# instagram régule le nombre de like à 1000 par heure ( dépassement => bloque le compte pour 24 h )
# instagram régule le nombre de commentaire efféctué par le robot d'affilé à 5 ( dépassement => bloque le commentaire )

# il faut cliquer à la main sur la photo une fois que la page en question est ouverte ( Sécurité pour ne pas se tromper de page )

### import des bibliotheques

import re
from selenium import webdriver as wd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time as t

### Variables

driver = wd.Firefox() # défini le browser firefox par défaut
insta_URL = "https://www.instagram.com/accounts/login/"
insta_id = "tibo.hnq@yahoo.com"
insta_pwd = "Tibonobo2397!"
compte = "raid" # page à aller liker

nb_img = 100 # entrer le nombre de photo à liker ( ATENTION A NE PAS DEPASSER 1000 PAR HEURE )
com = False # True = commentaires activés  /   False = commentaires désactivés
commentaire = "nice !" # si la fonctionnalité commentaire est activé, le robot commentera ce texte ( attention à ne pas oublier les apostrophes )

### Se connecter sur instagram

driver.get(insta_URL) # ouvre instagram
# driver.maximize_window() # plein écran

fermer = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/button[1]"))) # défini le bouton fermer
fermer.click() # click sur le bouton

username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username"))) # défini la zone de usename
username.send_keys(insta_id) # écrit dans la case séléctionné

password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
password.send_keys(insta_pwd)
password.send_keys(Keys.RETURN)

btn_Plustard = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")))
btn_Plustard.click()

ok = False
while ok == False :
    try:
        btn_Plustard = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]")))
        btn_Plustard.click()
        ok = True
    except :
        print("Retry to click on the 'plus tard' button")
        pass

# appuyer sur entrer

print(t.ctime())

### liker les photos

barre_de_recherche = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")))
barre_de_recherche.send_keys(compte)

t.sleep(1) # attend 1 seconde

pop = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div")))
pop.click()

#########------------Cliquer sur l'image-----------##############

s=1 # initialise le nombre de photo likée

print('Photos likées : '+str(s)+' / '+str(nb_img))
for i in range (nb_img-1): # parcours les photos une par une
    s+=1

    try: # essaye de liker la photo
        like = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[2]/section[1]/span[1]/button/div/span/svg")))
        print("Coeur détecté")
        if "J'aime" in like.get_attribute("aria-label") :
            like.click()

    except : # si il y a une erreur => renvoie une erreur sur le shell
        print('Erreur ;(')

    finally: # commente ( ou pas ) le post et passe à la suivante
        if com==True : # si la fonctionnalité com est activé, le robot va commenter le post
            btn_com =WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[2]/button/span")))
            btn_com.click()
            type = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/textarea")))
            type.send_keys(commentaire)
            send = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/button")))
            send.click()

        next = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div/div/a")))
        next.click()
        print('Photos likées : '+str(s)+' / '+str(nb_img))
        # t.sleep(4)