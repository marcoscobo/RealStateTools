import matplotlib.pyplot as plt
import numpy as np


## Variables simuladas
cap_ini = 0
cap_mes = 500
anios_sim = 30
interes_anual = 0.05
meses_sim = anios_sim * 12

## Cálculo de patrimonio acumulado
meses = np.arange(1, meses_sim + 1)
invertidos, acumulados = [cap_ini], [cap_ini]
for mes in meses:
    invertido = cap_ini + cap_mes * mes
    acumulado = cap_ini * (1 + interes_anual / 12) ** mes + cap_mes * ((1 + interes_anual / 12) ** mes - 1) / ((1 + interes_anual / 12) - 1)
    invertidos.append(round(invertido, 2))
    acumulados.append(round(acumulado, 2))

fig, ax = plt.subplots()
meses = [0] + list(meses)
years = np.arange(0, anios_sim + 1, 5)
years_starts = [y * 12 for y in years]
line = ax.plot(meses, invertidos, '--', label='invertido')
line = ax.plot(meses, acumulados, '-', label='acumulado', color='green')
ax.set_title('Patrimonio (€) por años')
ax.legend()
ax.set_xticks(years_starts)
ax.set_xticklabels(years)
ax.margins(y=0.1)
fig.tight_layout()
plt.show()