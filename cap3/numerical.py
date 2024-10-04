import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
r = 1.5
K = 10.0
V0 = 0.01
t0 = 0.0
tf = 5.0  # Ajuste o tempo final para se adequar ao intervalo do gráfico
dt = 0.1

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

# Solução
t, V = runge_kutta_4(dVdt, V0, t0, tf, dt)

# Configuração dos gráficos
listt = t
listV = V
listK = [K] * len(t)  # Linha horizontal para K

plt.plot(listt, listV, color='blue', label='V(t)')
plt.plot(listt, listK, '--', color='red', label='K')
plt.gca().set_xticks([])
plt.gca().set_yticks([])
plt.xlabel("Tempo", fontsize=20)
plt.ylabel("Volume", fontsize=20)
plt.xlim(0, 5)

# Adicionar anotações
plt.text(-0.25, V0, r'$V_{0}$', fontsize=12, color='black')
plt.text(-0.2, 9.9, r'$K$', fontsize=12, color='black')

plt.legend()
plt.savefig("numerical.png")
plt.show()
