import matplotlib.pyplot as plt
import numpy as np


class inmuebles:

    def __init__(self, cap_mes, num_pisos, anios_sim, valor_piso=100000, cuota_hip_piso=400, anios_hip_piso=30,
                 valor_reforma_piso=8000, entrada_hipoteca_piso=0.2, itp_piso=0.1, gestion_piso=0.015,
                 cashflow_mes_piso=100, anios_pasados=0):
        self.cap_mes = cap_mes
        self.num_pisos = num_pisos
        self.anios_sim = anios_sim
        self.valor_piso = valor_piso
        self.cuota_hip_piso = cuota_hip_piso
        self.anios_hip_piso = anios_hip_piso
        self.deuda_piso = self.cuota_hip_piso * self.anios_hip_piso * 12
        self.valor_reforma_piso = valor_reforma_piso
        self.entrada_hipoteca_piso = entrada_hipoteca_piso
        self.itp_piso = itp_piso
        self.gestion_piso = gestion_piso
        self.cap_necesario = self.valor_piso * (self.entrada_hipoteca_piso + self.itp_piso + self.gestion_piso) \
                             + self.valor_reforma_piso
        self.cashflow_mes_piso = cashflow_mes_piso
        self.anios_pasados = anios_pasados
        self.meses_sim = self.anios_sim * 12
        self.meses_pasados = 12 * self.anios_pasados
        self.meses = None
        self.anios = None
        self.valor = None
        self.valores = None
        self.deuda = None
        self.deudas = None
        self.capital = None
        self.capitales = None
        self.num_pisos_cum = None
        self.anios = None
        self.anios = None
        self.fig = None
        self.ax = None
        self.fig2 = None
        self.ax2 = None

    def calcular_meses(self):
        self.meses = []
        for i in range(self.num_pisos):
            n = round(self.cap_necesario / (self.cap_mes + self.cashflow_mes_piso * i))
            self.meses.append(n)
        self.anios = [round(m / 12, 1) for m in self.meses]

    def calcular_patrimonio(self):
        self.valor, self.valores, self.deuda, self.deudas, self.capital, self.capitales, self.num_pisos_cum = \
            0, [], 0, [], 0, [], 0
        for mes in range(self.meses[0], self.meses_sim + 1):
            if mes in np.cumsum(self.meses):
                self.valor += self.valor_piso
                self.deuda += self.deuda_piso
                self.num_pisos_cum += 1
            if self.num_pisos_cum < self.num_pisos:
                self.deuda -= self.cuota_hip_piso * self.num_pisos_cum
            else:
                if self.deuda > 0:
                    self.deuda -= self.cuota_hip_piso * self.num_pisos + self.cap_mes
                else:
                    self.deuda -= self.cap_mes
            self.capital = self.valor - self.deuda
            self.valores.append(self.valor)
            self.deudas.append(self.deuda)
            self.capitales.append(self.capital)

        self.valores = [0] * self.meses[0] + self.valores
        self.deudas = [0] * self.meses[0] + self.deudas
        self.capitales = [0] * self.meses[0] + self.capitales
        self.valores = np.array(self.valores)
        self.deudas = np.array(self.deudas)
        self.capitales = np.array(self.capitales)
        self.deudas[self.deudas < 0] = 0

    def representar_meses(self):
        self.fig, self.ax = plt.subplots()
        x_labels = ['Piso ' + str(i) for i in range(1, len(self.meses) + 1)]
        bars = self.ax.bar(x_labels, self.meses)
        self.ax.set_title('Número de meses (años) necesarios por piso')
        self.ax.bar_label(bars, label_type='edge', padding=3)
        self.ax.bar_label(bars, self.anios, label_type='edge', padding=-16, color='white')
        self.ax.bar_label(bars, ['({})'.format(i) for i in np.around(np.cumsum(self.anios), 1)], label_type='edge',
                     padding=-32, color='white')
        self.ax.margins(y=0.1)
        self.fig.tight_layout()
        plt.show()

    def representar_patrimonio(self, ):
        self.fig2, self.ax2 = plt.subplots()
        years = np.arange(0, self.anios_sim + 1 - self.anios_pasados, 5)
        years_starts = [y * 12 + self.meses_pasados for y in years]
        line = self.ax2.plot(range(self.meses_sim + 1)[self.meses_pasados:], self.valores[self.meses_pasados:],
                       '--', label='valor')
        line = self.ax2.plot(range(self.meses_sim + 1)[self.meses_pasados:], self.deudas[self.meses_pasados:],
                       '--', label='deuda')
        line = self.ax2.plot(range(self.meses_sim + 1)[self.meses_pasados:], self.capitales[self.meses_pasados:],
                       '-', label='patrimonio')
        self.ax2.set_title('Patrimonio (€) por años')
        self.ax2.legend()
        self.ax2.set_xticks(years_starts)
        self.ax2.set_xticklabels(years)
        self.ax2.margins(y=0.1)
        self.fig2.tight_layout()
        plt.show()

    def simular(self, verbose=True, plot_meses=False, plot_patrimonio=False):
        self.calcular_meses()
        self.calcular_patrimonio()
        if verbose:
            print('Número de inmuebles a los {} años: {}'.format(self.anios_sim, self.num_pisos_cum))
            print('Deuda a los {} años: {}€'.format(self.anios_sim, self.deuda))
            print('Patrimonio real a los {} años: {}€'.format(self.anios_sim, self.capital))
        if plot_meses:
            self.representar_meses()
        if plot_patrimonio:
            self.representar_patrimonio()
