from utils.inmuebles_tiempo import inmuebles
from utils.renta_variable_tiempo import renta_variable
import matplotlib.pyplot as plt
import numpy as np

def simular_patrimonio(anios_sim, num_pisos, interes_anual, cap_mes_inmuebles, cap_mes_renta_variable,
                       verbose=True, plot=True, save=None):

    sim_inmuebles = inmuebles(cap_mes=cap_mes_inmuebles, num_pisos=num_pisos, anios_sim=anios_sim)
    if verbose:
        print('-' * 40)
    sim_inmuebles.simular(verbose=verbose)
    sim_renta_variable = renta_variable(cap_ini=0, cap_mes=cap_mes_renta_variable, anios_sim=anios_sim,
                                        interes_anual=interes_anual)
    if verbose:
        print('-' * 40)
    sim_renta_variable.simular(verbose=verbose)
    if verbose:
        print('-' * 40)
        print('Patrimonio total a los {} años: {}€'.
              format(anios_sim,round(sim_inmuebles.capital + sim_renta_variable.acumulado)))
        print('-' * 40)

    if plot:
        plt.figure(figsize=(16, 9))
        plot1 = plt.subplot2grid((4, 6), (0, 0), rowspan=3, colspan=2)
        plot2 = plt.subplot2grid((4, 6), (0, 2), rowspan=2, colspan=4)
        plot3 = plt.subplot2grid((4, 6), (2, 2), rowspan=2, colspan=4)
        plot4 = plt.subplot2grid((4, 6), (3, 0), rowspan=1, colspan=2)

        x_labels = ['Piso ' + str(i) for i in range(1, len(sim_inmuebles.meses) + 1)]
        bars = plot1.bar(x_labels, sim_inmuebles.meses)
        plot1.set_title('Número de meses (años) necesarios por piso')
        plot1.bar_label(bars, label_type='edge', padding=3)
        plot1.bar_label(bars, sim_inmuebles.anios, label_type='edge', padding=-16, color='white')
        plot1.bar_label(bars, ['({})'.format(i) for i in np.around(np.cumsum(sim_inmuebles.anios), 1)], label_type='edge',
                     padding=-32, color='white')
        plot1.margins(y=0.1)

        years = np.arange(0, sim_inmuebles.anios_sim + 1 - sim_inmuebles.anios_pasados, 5)
        years_starts = [y * 12 + sim_inmuebles.meses_pasados for y in years]
        plot2.plot(range(sim_inmuebles.meses_sim + 1)[sim_inmuebles.meses_pasados:],
                             sim_inmuebles.valores[sim_inmuebles.meses_pasados:],
                             '--', label='valor')
        plot2.plot(range(sim_inmuebles.meses_sim + 1)[sim_inmuebles.meses_pasados:],
                             sim_inmuebles.deudas[sim_inmuebles.meses_pasados:],
                             '--', label='deuda')
        plot2.plot(range(sim_inmuebles.meses_sim + 1)[sim_inmuebles.meses_pasados:],
                             sim_inmuebles.capitales[sim_inmuebles.meses_pasados:],
                             '-', label='patrimonio')
        plot2.set_title('Patrimonio (€) en inmuebles por años')
        plot2.legend()
        plot2.set_xticks(years_starts)
        plot2.set_xticklabels(years)
        plot2.margins(y=0.1)

        years = np.arange(0, sim_renta_variable.anios_sim + 1, 5)
        years_starts = [y * 12 for y in years]
        plot3.plot(sim_renta_variable.meses, sim_renta_variable.invertidos, '--', label='invertido')
        plot3.plot(sim_renta_variable.meses, sim_renta_variable.acumulados, '-', label='acumulado', color='green')
        plot3.set_title('Patrimonio (€) en renta variable por años')
        plot3.legend()
        plot3.set_xticks(years_starts)
        plot3.set_xticklabels(years)
        plot3.margins(y=0.1)

        plot4.plot(sim_renta_variable.meses, sim_inmuebles.capitales + sim_renta_variable.acumulados, label='invertido')
        plot4.fill_between(sim_renta_variable.meses, sim_inmuebles.capitales + sim_renta_variable.acumulados, label='invertido', alpha=0.75)
        plot4.set_title('Patrimonio (€) total por años')

        plt.tight_layout()
        if save is not None:
            plt.savefig(save)
        plt.show()