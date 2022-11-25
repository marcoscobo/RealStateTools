import matplotlib.pyplot as plt
import numpy as np


valor_piso = 100000
valor_reforma = 8000
entrada_hipoteca = 0.2
itp = 0.1
gestion = 0.015
cap_necesario = valor_piso * (entrada_hipoteca + itp + gestion) + valor_reforma

cashflow_mes = 100
cap_mes = 500

num_pisos = 5

meses = []
for i in range(num_pisos):
    n = round(cap_necesario / (cap_mes + cashflow_mes * i))
    meses.append(n)

anios = [round(m / 12, 1) for m in meses]

valores = [valor_piso] * num_pisos



fig, ax = plt.subplots()
x_labels = ['Piso ' + str(i) for i in range(1, len(meses) + 1)]
bars = ax.bar(x_labels, meses)
ax.set_title('Número de meses (años) necesarios por número de pisos')
ax.bar_label(bars, label_type='edge', padding=3)
ax.bar_label(bars, anios, label_type='edge', padding=-16, color='white')
ax.margins(y=0.1)
fig.tight_layout()
plt.show()


fig, ax = plt.subplots()
line = ax.plot(np.cumsum([0] + anios), np.cumsum([0] + valores), 'o--')
fig.tight_layout()
plt.show()
