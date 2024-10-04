import numpy as np
import matplotlib.pyplot as plt

# Definindo a função dx/dt
def dxdt(x, h):
    return x * (1 - x) - h

# Função que implementa o método de Runge-Kutta de quarta ordem
def runge_kutta(f, x0, t0, t_final, h, dt):
    t = np.arange(t0, t_final, dt)
    x = np.zeros(len(t))
    x[0] = x0

    for i in range(1, len(t)):
        k1 = dt * f(x[i-1], h)
        k2 = dt * f(x[i-1] + 0.5 * k1, h)
        k3 = dt * f(x[i-1] + 0.5 * k2, h)
        k4 = dt * f(x[i-1] + k3, h)
        x[i] = x[i-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t, x


Ngrafic = 10

hlist = np.linspace(0.24, 0.26, Ngrafic)
for i in range(Ngrafic):

    # Parâmetros do problema
    h = hlist[i]      # Constante
    x0 = 0.5          # Condição inicial para x
    t0 = 0            # Tempo inicial
    t_final = 10      # Tempo final
    dt = 0.001        # Passo de tempo

    # Resolvendo a equação usando Runge-Kutta
    t, x = runge_kutta(dxdt, x0, t0, t_final, h, dt)

    # Gerando o gráfico de campo vetorial
    x_vals = np.linspace(-0.5, 1.5, 20)   # Ajustar densidade
    t_vals = np.linspace(0, t_final, 20)  # Ajustar densidade
    X, T = np.meshgrid(x_vals, t_vals)
    dXdt = dxdt(X, h)

    # Intensidade dos vetores (para colorir de acordo com a magnitude)
    intensity = np.sqrt(1**2 + dXdt**2)

    # Plotando o campo vetorial com setas maiores e espaçamento ajustado
    plt.figure(figsize=(8, 6))
    plt.quiver(T, X, np.ones(T.shape), dXdt, intensity, angles='xy', scale_units='xy', scale=8, cmap='plasma', width=0.005)  # Ajuste de escala e largura
    plt.colorbar(label='Intensidade (Magnitude)')

    # Plotando a trajetória da solução
    plt.plot(t, x, color='red', label=f"Trajetória com h = {h}")
    plt.title(f"Campo Vetorial com Intensidade de Cores e Trajetória h = {h}")
    plt.xlabel(r"Tempo ($\tau$)")
    plt.ylabel("População (x)")
    #plt.ylim(0.4, 0.6)
    plt.grid(True)
    plt.legend()

    # Salvando o gráfico
    plt.savefig(f"fig{i}.png")
    #plt.show()
