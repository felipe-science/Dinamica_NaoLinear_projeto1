import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Definindo a função f(x, h)
def f(x, h):
    return x * (1 - x) - h

# Faixa de valores de h
h_values = np.linspace(0, 0.5, 200)  # Aumentando a densidade de valores
fixed_points = []

# Encontrando os pontos fixos para cada valor de h
for h in h_values:
    # Usando fsolve para encontrar as raízes da função f(x, h)
    roots = []
    
    # Tentando diferentes estimativas iniciais
    initial_guesses = np.linspace(0, 1, 10)  # Usando 10 valores de estimativa inicial entre 0 e 1
    for initial_guess in initial_guesses:
        root = fsolve(f, initial_guess, args=(h), xtol=1e-6, maxfev=1000)  # Ajustando tolerância e número máximo de iterações
        
        # Adicionando apenas raízes válidas dentro do intervalo [0, 1]
        if 0 <= root[0] <= 1 and root[0] not in roots:
            roots.append(root[0])
    
    # Adicionando raízes ao conjunto de pontos fixos
    for root in roots:
        fixed_points.append((h, root))

fixed_points = np.array(fixed_points)

# Plotando os pontos fixos em relação a h
plt.figure(figsize=(10, 6))

# Aplicando as cores conforme as condições especificadas
for h, x in fixed_points:
    if h < 0.25 and x > 0.5:
        plt.scatter(h, x, color='black')  # Preto
    elif h < 0.25 and x < 0.5:
        plt.scatter(h, x, color='white', edgecolor='black')  # Branco com contorno preto
    elif h >= 0.25:  # Para h >= 0.25, mantenha a cor azul
        plt.scatter(h, x, color='gray')

plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axhline(1, color='black', lw=0.5, ls='--')
plt.axvline(0.25, color='red', linestyle='--', label='Bifurcação em h = 0.25')

# Adicionando detalhes ao gráfico
plt.title(r"Análise de Bifurcação em $h_{c} = 0.25$", fontsize='20')
plt.xlabel(r"$h$", fontsize='15')
plt.ylabel(r"Ponto Fixo $(x)$", fontsize='15')
plt.ylim(-0.1, 1.1)
plt.grid(True)
plt.legend(fontsize='15', loc='upper right')
plt.tick_params(axis='both', which='major', labelsize=12)  # Altera o tamanho dos ticks principais
plt.savefig("fork.png", dpi=500)
plt.show()
