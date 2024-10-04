import numpy as np
import matplotlib.pyplot as plt
from numpy import linspace, exp, log

# Parâmetros
r = 1.5
K = 10.0
V0 = 0.01
t0 = 0.0
tf = 5.0  # Tempo final
dt = 0.1  # Passo de tempo

# Função analítica
def functionV(K, V0, r, t0):
    listt = linspace(0, tf, 100)
    listV = K * exp(log(V0 / K) * np.exp(-r * (listt - t0)))
    listK = [K] * len(listt)
    return listt, listV, listK

# Função que define a equação diferencial
def dVdt(V, t):
    return r * V * (np.log(K) - np.log(V))

# Método de Runge-Kutta de 4ª ordem
def runge_kutta_4(dVdt, V0, t0, tf, dt):
    num_steps = int((tf - t0) / dt)
    t = np.linspace(t0, tf, num_steps + 1)
    V = np.zeros(num_steps + 1)
    V[0] = V0

    for i in range(num_steps):
        k1 = dt * dVdt(V[i], t[i])
        k2 = dt * dVdt(V[i] + 0.5 * k1, t[i] + 0.5 * dt)
        k3 = dt * dVdt(V[i] + 0.5 * k2, t[i] + 0.5 * dt)
        k4 = dt * dVdt(V[i] + k3, t[i] + dt)
        V[i + 1] = V[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t, V

# Calcular soluções
t_analitico, V_analitico, K_analitico = functionV(K, V0, r, t0)
t_numerico, V_numerico = runge_kutta_4(dVdt, V0, t0, tf, dt)

# Plotar as soluções
plt.figure(figsize=(10, 6))

# Solução analítica
plt.plot(t_analitico, V_analitico, linestyle='-', color='blue', label='Solução Analítica')

# Solução numérica
plt.plot(t_numerico, V_numerico, color='red', linestyle='--', label='Solução Numérica')

# Linha horizontal para K
plt.plot(t_analitico, K_analitico, linestyle='--', color='green', label='K')

# Configurações do gráfico
plt.gca().set_xticks([])
plt.gca().set_yticks([])
plt.xlabel("Tempo", fontsize=20)
plt.ylabel("Volume", fontsize=20)
plt.title("Modelo de Gompertz", fontsize='22')
plt.xlim(0, 5)

# Adicionar anotações
plt.text(-0.25, V0, r'$V_{0}$', fontsize=12, color='black')
plt.text(-0.2, 9.9, r'$K$', fontsize=12, color='black')

plt.legend(loc = 'best', fontsize = '15')
plt.savefig("solucoes_combinadas.png")
plt.show()
