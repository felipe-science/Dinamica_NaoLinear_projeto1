import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do modelo
alpha = 0.1  # Coeficiente de crescimento
beta = 0.2   # Coeficiente de feedback
D1 = 0.05    # Intensidade do ruído multiplicativo
Q = 0.01     # Intensidade do ruído aditivo
lambda_1 = 0.1  # Coeficiente de acoplamento
T = 10.0     # Tempo total da simulação
dt = 0.01    # Passo de tempo
N = int(T / dt)  # Número de passos de tempo

# Inicialização
x = np.zeros(N)
x[0] = 1.0  # Condição inicial
t = np.linspace(0, T, N)

# Simulação usando o método de Euler-Maruyama
for i in range(1, N):
    # Gerar ruído branco gaussiano
    epsilon = np.random.normal(0, 1)  # Ruído multiplicativo
    Lambda = np.random.normal(0, np.sqrt(Q))  # Ruído aditivo

    # Atualização da variável x
    dx = (alpha * x[i-1] - beta * x[i-1] * np.log(x[i-1])) * dt + \
         (x[i-1] * epsilon * np.sqrt(D1) + Lambda) * dt

    x[i] = x[i-1] + dx

# Plotagem dos resultados
plt.figure(figsize=(12, 6))
plt.plot(t, x, label='Solução da EDE', color='blue')
plt.title('Solução da Equação Diferencial Estocástica')
plt.xlabel('Tempo (t)')  # Título do eixo X
plt.ylabel('Valor de x(t)')  # Título do eixo Y
plt.legend()
plt.grid()
plt.show()
