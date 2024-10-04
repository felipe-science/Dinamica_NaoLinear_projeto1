
import numpy as np
import matplotlib.pyplot as plt

# Definindo a equação diferencial dx/dτ = x(1 - x) - h
def dxdt(x, h):
    return x * (1 - x) - h

# Implementando o método de Runge-Kutta de quarta ordem
def runge_kutta(f, x0, t0, t_final, h, dt):
    t = np.arange(t0, t_final, dt)  # Vetor de tempo
    x = np.zeros(len(t))            # Soluções para x em diferentes instantes
    x[0] = x0                       # Condição inicial

    # Método de Runge-Kutta
    for i in range(1, len(t)):
        k1 = dt * f(x[i-1], h)
        k2 = dt * f(x[i-1] + 0.5 * k1, h)
        k3 = dt * f(x[i-1] + 0.5 * k2, h)
        k4 = dt * f(x[i-1] + k3, h)
        x[i] = x[i-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t, x

# Parâmetros do problema
h = 0.248      # Constante h (pode variar)
x0 = 0.5    # Condição inicial para x
t0 = 0       # Tempo inicial
t_final = 10 # Tempo final
dt = 0.001    # Passo de tempo

# Resolvendo a equação usando Runge-Kutta para um valor de h
t, x = runge_kutta(dxdt, x0, t0, t_final, h, dt)

# Gerando o gráfico
plt.figure(figsize=(8, 6))
plt.plot(t, x, label=f'Solução para h={h}')
plt.title(r'Solução da equação $\frac{dx}{d\tau} = x(1 - x) - h$')
plt.xlabel(r'Tempo ($\tau$)')
plt.ylabel('População (x)')
plt.grid(True)
plt.legend()
plt.show()
