import numpy as np
import pylab as plt

# Solução das raizes
listx = np.linspace(0, 1, 1000)
listh = (1 - (2 * listx - 1)**2) / 4

estavel_listx = listx[:len(listx)//2]
estavel_listh = listh[:len(listh)//2]
instavel_listx = listx[len(listx)//2:]
instavel_listh = listh[len(listh)//2:]

# Reta vertical
xvert = []
yvert = np.linspace(-0.2, 1.2, 1000)
for i in range(len(yvert)):
    xvert.append(0.25)

# Criar o gráfico
plt.plot(estavel_listh, estavel_listx, color='blue', linestyle='--')
plt.plot(instavel_listh, instavel_listx, color='blue')
plt.plot(xvert, yvert, color='red')

# Adicionar rótulos e texto
plt.xlabel(r"$h$", fontsize=20)
plt.ylabel(r"$x$", fontsize=20)
plt.text(0.0, -0.1, 'Instável', fontsize=15)
plt.text(0.0, 1.01, 'Estável', fontsize=15)

# Ajustar parâmetros dos ticks
plt.tick_params(axis='both', which='major', labelsize=14, length=10, width=2)

# Adicionar grade
plt.grid(True)

# Aumentar as margens da figura
plt.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.15)

# Mostrar o gráfico
plt.savefig("figaa.png", dpi=300)
plt.show()
