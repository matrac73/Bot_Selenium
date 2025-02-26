from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = wd.Firefox()
URL = "https://www.interphex.com/en-us/show-info/exhibitor-list.html?refinementList%5B0%5D%5B0%5D=exhibitorFilters.Product%20Categories.lvl0%3Aid-681441&refinementList%5B0%5D%5B1%5D=exhibitorFilters.Product%20Categories.lvl0%3Aid-681634#/"

driver.get(URL)

# PIN.send_keys("Bonjour") # Ecrire dans une zone

# PIN.send_keys(Keys.RETURN) # Appuyer sur entrer

# NICKNAME = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="test"]"""))) # Selectionner une balise

# NICKNAME.click() # clicker

# driver.execute_script("window.open();") # ouvrir nouvel onglet
# window_after = driver.window_handles[1] # définir onglet
# driver.switch_to.window(window_after) # changer onglet
