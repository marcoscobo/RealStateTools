import matplotlib.pyplot as plt
import numpy as np

## Variables piso
valor_piso = 100000
cuota_hip_piso = 400
anios_hip_piso = 30
deuda_piso = cuota_hip_piso * anios_hip_piso * 12
valor_reforma_piso = 8000
entrada_hipoteca_piso = 0.2
itp_piso = 0.1
gestion_piso = 0.015
cap_necesario = valor_piso * (entrada_hipoteca_piso + itp_piso + gestion_piso) + valor_reforma_piso
cashflow_mes_piso = 100

## Variables simuladas
cap_mes = 500
num_pisos = 3
anios_sim = 30
anios_pasados = 0
meses_sim = anios_sim * 12
meses_pasados = 12 * anios_pasados


## Calculo de meses necesarios
meses = []
for i in range(num_pisos):
    n = round(cap_necesario / (cap_mes + cashflow_mes_piso * i))
    meses.append(n)
anios = [round(m / 12, 1) for m in meses]

## Cálculo de valor, deuda y patrimonio acumulado
valor, valores, deuda, deudas, capital, capitales, num_pisos_cum = 0, [], 0, [], 0, [], 0
for mes in range(meses[0], meses_sim + 1):
    if mes in np.cumsum(meses):
        valor += valor_piso
        deuda += deuda_piso
        num_pisos_cum += 1
    if num_pisos_cum < num_pisos:
        deuda -= cuota_hip_piso * num_pisos_cum
    else:
        if deuda > 0:
            deuda -= cuota_hip_piso * num_pisos + cap_mes
        else:
            deuda -= cap_mes
    capital = valor - deuda
    valores.append(valor)
    deudas.append(deuda)
    capitales.append(capital)

valores = [0] * meses[0] + valores
deudas = [0] * meses[0] + deudas
capitales = [0] * meses[0] + capitales
valores = np.array(valores)
deudas = np.array(deudas)
capitales = np.array(capitales)
deudas[deudas < 0] = 0


## Gráfico de Número de meses (años) necesarios por piso
fig, ax = plt.subplots()
x_labels = ['Piso ' + str(i) for i in range(1, len(meses) + 1)]
bars = ax.bar(x_labels, meses)
ax.set_title('Número de meses (años) necesarios por piso')
ax.bar_label(bars, label_type='edge', padding=3)
ax.bar_label(bars, anios, label_type='edge', padding=-16, color='white')
ax.bar_label(bars, ['({})'.format(i) for i in np.around(np.cumsum(anios), 1)], label_type='edge', padding=-32, color='white')
ax.margins(y=0.1)
fig.tight_layout()
plt.show()

## Gráfico de Patrimonio (€) por años
fig, ax = plt.subplots()
years = np.arange(0, anios_sim + 1 - anios_pasados, 5)
years_starts = [y * 12 + meses_pasados for y in years]
line = ax.plot(range(meses_sim + 1)[meses_pasados:], valores[meses_pasados:], '--', label='valor')
line = ax.plot(range(meses_sim + 1)[meses_pasados:], deudas[meses_pasados:], '--', label='deuda')
line = ax.plot(range(meses_sim + 1)[meses_pasados:], capitales[meses_pasados:], '-', label='patrimonio')
ax.set_title('Patrimonio (€) por años')
ax.legend()
ax.set_xticks(years_starts)
ax.set_xticklabels(years)
ax.margins(y=0.1)
fig.tight_layout()
plt.show()
