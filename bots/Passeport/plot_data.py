import matplotlib.pyplot as plt
import numpy as np
import csv
import time

with open('data_dispo.csv', 'r') as f:
    obj = csv.reader(f)
    X, Y = [], []
    for ligne in obj:
        if len(ligne) != 0:
            Y.append(int(ligne[0]))
            X.append(ligne[1])

fig = plt.figure(figsize=(12, 6))
plt.plot(X,Y)
plt.title('Places disponibles')
plt.grid()
ax = plt.gca()
ax.get_xaxis().set_visible(False)
plt.show()
time.sleep(2)
plt.close(fig)
