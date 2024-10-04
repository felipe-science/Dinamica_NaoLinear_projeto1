import numpy as np
import pylab as plt

def xpont(h):
    listx = np.linspace(-0.1, 1.1, 1000)
    listy = listx * (1 - listx) - h
    return listx, listy

def raizes(h):
    x1 = (1 + np.sqrt(1 - 4 * h)) / 2.0
    x2 = (1 - np.sqrt(1 - 4 * h)) / 2.0
    return x1, x2

# Lista de valores de h
listh = [0.23, 0.24, 0.25, 0.26, 0.27]
for h in listh:
    xlist, ylist = xpont(h)
    x1, x2 = raizes(h)
    
    if h == 0.25:
        plt.plot(xlist, ylist, label=rf'$h = {round(h, 2)}$')
        plt.scatter(x1, 0.0, color="gray", edgecolor="black")
        plt.scatter(x2, 0.0, color="gray", edgecolor="black")
    else:
        plt.plot(xlist, ylist, label=rf'$h = {round(h, 2)}$')
        plt.scatter(x1, 0.0, color="black", edgecolor="black")
        plt.scatter(x2, 0.0, color="white", edgecolor="black")

# Eixo x = 0
xzero = np.linspace(-0.1, 1.1, 1000)
yzero = np.zeros_like(xzero)  # Usando np.zeros_like para simplificar
plt.plot(xzero, yzero, linestyle='--', color='red')

# Configurações do gráfico
plt.legend(loc='best')
plt.grid(True)
plt.xlabel(r"$x$", fontsize='20')
plt.ylabel(r"$f(x)$", fontsize='20')  # Corrigido: de xlabel para ylabel
plt.tick_params(axis='both', which='major', labelsize=15)
plt.xlim(0.25, 0.75)
plt.ylim(-0.03, 0.025)

# Aumentando as margens ainda mais
plt.subplots_adjust(left=0.2, right=0.9, top=0.95, bottom=0.2)  # Ajuste as margens conforme necessário

# Exibindo o gráfico
plt.savefig("selano.png", dpi=300)
plt.show()
