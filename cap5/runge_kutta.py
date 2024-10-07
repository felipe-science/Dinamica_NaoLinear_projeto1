from vpython import *
import numpy as np

# Parâmetros do sistema
m = 1.0   # massa
b = 0.5   # constante de amortecimento (b > 0)
k = 1.0   # constante elástica
h = 0.01  # passo de tempo
t_max = 20.0  # tempo total de simulação

# Condições iniciais
x0 = 1.0  # posição inicial
v0 = 0.0  # velocidade inicial
n = int(t_max / h)  # número de passos

# Inicialização dos arrays
t = np.linspace(0, t_max, n)
x = np.zeros(n)
v = np.zeros(n)

# Condições iniciais
x[0] = x0
v[0] = v0

# Função que define o sistema de equações
def f(t, x, v):
    return v, -b/m * v - k/m * x

# Método de Runge-Kutta de quarta ordem
for i in range(n-1):
    k1_x, k1_v = f(t[i], x[i], v[i])
    k2_x, k2_v = f(t[i] + h/2, x[i] + h/2 * k1_x, v[i] + h/2 * k1_v)
    k3_x, k3_v = f(t[i] + h/2, x[i] + h/2 * k2_x, v[i] + h/2 * k2_v)
    k4_x, k4_v = f(t[i] + h, x[i] + h * k3_x, v[i] + h * k3_v)

    x[i+1] = x[i] + (h/6) * (k1_x + 2*k2_x + 2*k3_x + k4_x)
    v[i+1] = v[i] + (h/6) * (k1_v + 2*k2_v + 2*k3_v + k4_v)




# Criar a cena VPython
scene = canvas(title='Simulação de um Oscilador Harmônico com Mola', width=800, height=400)

# Criar a mola
spring = helix(pos=vector(-1.2, 0.0, 0.0), axis=vector(0, 0, 0), radius=0.06, coils=40, color=color.green)

# Criar a caixa
box_mass = box(pos=vector(2, 0.0, 0.0), size=vector(0.2, 0.2, 0.2), color=color.red)




# Criar os eixos cartesianos
# Eixo X
curve(pos=[vector(-1.1, 0, 0), vector(1.1, 0, 0)], radius=0.01, color=color.white)
# Eixo Y
curve(pos=[vector(0, -0.5, 0), vector(0, 0.5, 0)], radius=0.01, color=color.white)





# Animar o movimento da massa
for i in range(n):
    rate(100)  # Controla a velocidade da animação
    # Atualiza a posição da caixa
    box_mass.pos.x = x[i]
    # Atualiza a posição da mola
    spring.axis = vector(x[i], 0, 0) - spring.pos

# Finaliza a simulação
print("Simulação completa.")
