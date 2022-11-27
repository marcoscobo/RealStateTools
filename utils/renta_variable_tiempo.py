import matplotlib.pyplot as plt
import numpy as np


class renta_variable:

    def __init__(self, cap_ini, cap_mes, anios_sim, interes_anual):
        self.cap_ini = cap_ini
        self.cap_mes = cap_mes
        self.anios_sim = anios_sim
        self.interes_anual = interes_anual
        self.meses_sim = self.anios_sim * 12
        self.meses = None
        self.invertidos = None
        self.acumulados = None
        self.invertido = None
        self.acumulado = None
        self.fig = None
        self.ax = None

    def calcular(self):
        self.meses = np.arange(1, self.meses_sim + 1)
        self.invertidos, self.acumulados = [self.cap_ini], [self.cap_ini]
        for mes in self.meses:
            self.invertido = self.cap_ini + self.cap_mes * mes
            self.acumulado = self.cap_ini * (1 + self.interes_anual / 12) ** mes + self.cap_mes * (
                        (1 + self.interes_anual / 12) ** mes - 1) / ((1 + self.interes_anual / 12) - 1)
            self.invertidos.append(round(self.invertido, 2))
            self.acumulados.append(round(self.acumulado, 2))
        self.meses = [0] + list(self.meses)

    def representar(self):
        self.fig, self.ax = plt.subplots()
        years = np.arange(0, self.anios_sim + 1, 5)
        years_starts = [y * 12 for y in years]
        line = self.ax.plot(self.meses, self.invertidos, '--', label='invertido')
        line = self.ax.plot(self.meses, self.acumulados, '-', label='acumulado', color='green')
        self.ax.set_title('Patrimonio (€) por años')
        self.ax.legend()
        self.ax.set_xticks(years_starts)
        self.ax.set_xticklabels(years)
        self.ax.margins(y=0.1)
        self.fig.tight_layout()
        plt.show()

    def simular(self, verbose=True, plot=False):
        self.calcular()
        if verbose:
            print('Total invertido a los {} años: {}€'.format(self.anios_sim, int(self.invertido)))
            print('Total acumulado a los {} años: {}€'.format(self.anios_sim, round(self.acumulado)))
        if plot:
            self.representar()
