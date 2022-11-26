import matplotlib.pyplot as plt
import numpy as np


## Variables simuladas
cap_ini = 0
cap_mes = 500
anios_sim = 50
interes_anual = 0.07
meses_sim = anios_sim * 12
int_anual = 1 + interes_anual
int_mensual = int_anual ** (1 / 12)

## Cálculo de patrimonio acumulado
meses = np.arange(meses_sim + 1)
invertido, invertidos, acumulado, acumulados = 0, [], 0, []
