from utils.simular_patrimonio import simular_patrimonio

anios_sim = 30
num_pisos = 5
interes_anual = 0.05
cap_mes_inmuebles = 500
cap_mes_renta_variable = 500

simular_patrimonio(anios_sim, num_pisos, interes_anual, cap_mes_inmuebles, cap_mes_renta_variable,
                   save='figure.png')