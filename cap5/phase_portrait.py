import numpy as np
import matplotlib.pyplot as plt

# Definindo os parâmetros do sistema
m = 1.0  # massa
b = 0.0  # constante de amortecimento
k = 1.0  # constante da mola

# Função que define o sistema de equações diferenciais
def system(X):
    x, v = X  # x = posição, v = velocidade
    dxdt = v
    dvdt = -b/m * v - k/m * x  # Incluindo amortecimento
    return np.array([dxdt, dvdt])

# Método Runge-Kutta de quarta ordem
def runge_kutta_4th_order(X0, t):
    X = np.zeros((len(t), len(X0)))
    X[0] = X0
    
    for i in range(len(t) - 1):
        dt = t[i+1] - t[i]
        k1 = system(X[i])
        k2 = system(X[i] + 0.5 * dt * k1)
        k3 = system(X[i] + 0.5 * dt * k2)
        k4 = system(X[i] + dt * k3)
        X[i+1] = X[i] + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)

    return X

# Criando uma grade de pontos para o retrato de fase
x_vals = np.linspace(-3, 3, 20)
y_vals = np.linspace(-3, 3, 20)
X1, Y1 = np.meshgrid(x_vals, y_vals)

# Calcular as direções do vetor no campo
DX1, DY1 = np.zeros_like(X1), np.zeros_like(Y1)
for i in range(len(x_vals)):
    for j in range(len(y_vals)):
        xdot = system([X1[i, j], Y1[i, j]])
        DX1[i, j] = xdot[0]
        DY1[i, j] = xdot[1]

# Normalizando os vetores para a visualização
M = (np.hypot(DX1, DY1))
M[M == 0] = 1.  # evitar divisão por zero
DX1 /= M
DY1 /= M

# Criar o gráfico
plt.figure(figsize=(10, 8))
plt.quiver(X1, Y1, DX1, DY1, color='blue')
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.title('Retrato de Fase do Sistema Massa-Mola (Com Amortecimento)', fontsize='20')
plt.xlabel('Posição (x)', fontsize='15')
plt.ylabel('Velocidade (dx/dt)', fontsize='15')

# Desenhar linhas de trajetória para algumas condições iniciais
initial_conditions = [(-2, 2)]
t = np.linspace(0, 20, 1000)  # Criar uma linha do tempo

for (x0, v0) in initial_conditions:
    X = runge_kutta_4th_order([x0, v0], t)  # Integrar usando RK4
    plt.plot(X[:, 0], X[:, 1], lw=2, color = 'red')

# Adicionar o ponto fixo
plt.scatter(0, 0, color='black')  # Ponto fixo na origem
plt.grid()
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.show()
