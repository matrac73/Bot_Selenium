import re
from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time as t
import matplotlib.pyplot as plt

# Initialize lists to store the values
brut_salaries = []
cout_employeurs = []
net_avant_impots = []
net_apres_impots = []

driver = wd.Firefox()
Urssaf_URL = "https://mon-entreprise.urssaf.fr/simulateurs/salaire-brut-net"

driver.get(Urssaf_URL)
driver.maximize_window()

annuel_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((
        By.XPATH,
        """/html/body/div/div/div[2]/div/div/main/div/div/div/div[2]/div/div[1]/div[1]/div/div/div/div/div/span[2]/label/span/span[2]""")))
annuel_button.click()

# Enable interactive mode
plt.ion()

# Create a figure and axes object
fig, ax = plt.subplots(figsize=(10, 8))

# Initialize the lines for each curve
line_cout_employeurs, = ax.plot([], [], label='Coût total employeur')
line_brut_salaries, = ax.plot([], [], label='Brut')
line_net_avant_impots, = ax.plot([], [], label='Net avant impôt')
line_net_apres_impots, = ax.plot([], [], label='Net après impôt')

# Set the labels and title
ax.set_ylabel('Salaires')
ax.set_title('Évolution des montants')
ax.legend()
ax.grid(True)

# Set the x and y limits
ax.set_xlim(0, 100)
ax.set_ylim(0, 100000)


# Function to update the plot
def update_plot():
    line_cout_employeurs.set_data(range(len(cout_employeurs)), cout_employeurs)
    line_brut_salaries.set_data(range(len(brut_salaries)), brut_salaries)
    line_net_avant_impots.set_data(range(len(net_avant_impots)), net_avant_impots)
    line_net_apres_impots.set_data(range(len(net_apres_impots)), net_apres_impots)

    # Adjust the y-axis limit based on the maximum value
    ax.set_ylim(0, max(max(cout_employeurs), max(brut_salaries), max(net_avant_impots), max(net_apres_impots)))

    fig.canvas.draw()
    fig.canvas.flush_events()


for brut_salary in range(0, 100100, 100):
    brut = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="salarié___contrat___salaire_brut"]""")))
    brut.clear()
    brut.send_keys(str(brut_salary))

    t.sleep(5)

    cout_employeur = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="salarié___coût_total_employeur"]"""))).get_attribute("value")
    brut = brut.get_attribute("value")
    net_avant_impot = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="salarié___rémunération___net___à_payer_avant_impôt"]"""))).get_attribute("value")
    net_après_impot = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="salarié___rémunération___net___payé_après_impôt"]"""))).get_attribute("value")

    cout_employeur_pattern = re.findall(r'\d+', cout_employeur)
    brut_pattern = re.findall(r'\d+', brut)
    net_avant_impot_pattern = re.findall(r'\d+', net_avant_impot)
    net_après_impot_pattern = re.findall(r'\d+', net_après_impot)

    cout_employeur = int(''.join(cout_employeur_pattern))
    brut = int(''.join(brut_pattern))
    net_avant_impot = int(''.join(net_avant_impot_pattern))
    net_après_impot = int(''.join(net_après_impot_pattern))

    print(cout_employeur, brut, net_avant_impot, net_après_impot)

    # Append the values to the lists
    brut_salaries.append(brut)
    cout_employeurs.append(cout_employeur)
    net_avant_impots.append(net_avant_impot)
    net_apres_impots.append(net_après_impot)

    # Update the plot
    update_plot()

# Close the browser
driver.quit()

# Disable interactive mode
plt.ioff()

# Show the final plot
plt.show()
