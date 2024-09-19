import numpy as np
import pylab as plt

r = 0.1
V0 = 0.0
K = 10

def Vponto(r,K,V0):

    list0 = []
    Vplist = []
    Vlist = np.linspace(1e-6,10.5,1000)
    for V in Vlist:
        Vp = r*V*(np.log(K) - np.log(V))
        Vplist.append(Vp)
        


    return Vlist, Vplist



Vlist, Vplist= Vponto(r,K,V0)



listx0 = np.linspace(-5,15,1000)
listy0 = []
for x in listx0:
    listy0.append(0.0)



plt.plot(Vlist, Vplist, color="blue")
plt.plot(listx0, listy0, linestyle="--", color = "green")
plt.scatter(K,0.0, color="black", s=200, zorder=6)
plt.scatter(0.0, 0.0, color="white", edgecolor="black", s=200, zorder=5)  # Ajuste o tamanho com s
plt.title(f"$K = {K}$     $r = {r}$     $V_0 = {V0}$", fontsize=20)
plt.xlabel("V", fontsize = 15)
plt.ylabel(r"$\dot{V}$", fontsize = 15)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.grid("True")
plt.subplots_adjust(left=0.15, right=0.85, top=0.85, bottom=0.15)
plt.xlim(-1.0,12)



plt.annotate(
    '',  # Texto vazio, apenas a seta será desenhada
    xy=(9.5, 0),  # Ponto final da seta
    xytext=(8.5, 0),  # Ponto inicial da seta (mais próximo do ponto final)
    arrowprops=dict(
        facecolor='red',  # Cor da seta
        edgecolor='red',  # Cor da borda da seta
        arrowstyle='->',  # Estilo da seta
        linewidth=4  # Largura da linha da seta
    )
)




# Adicionar uma seta vindo do lado direito
plt.annotate(
    '',  # Texto vazio, apenas a seta será desenhada
    xy=(10.5, 0),  # Ponto final da seta
    xytext=(11.5, 0),  # Ponto inicial da seta (mais próximo do ponto final)
    arrowprops=dict(
        facecolor='red',  # Cor da seta
        edgecolor='red',  # Cor da borda da seta
        arrowstyle='->',  # Estilo da seta
        linewidth=4  # Largura da linha da seta
    )
)





# Adicionar uma seta vindo do lado direito
plt.annotate(
    '',  # Texto vazio, apenas a seta será desenhada
    xy=(1.5, 0),  # Ponto final da seta
    xytext=(0.5, 0),  # Ponto inicial da seta (mais próximo do ponto final)
    arrowprops=dict(
        facecolor='red',  # Cor da seta
        edgecolor='red',  # Cor da borda da seta
        arrowstyle='->',  # Estilo da seta
        linewidth=4  # Largura da linha da seta
    )
)


plt.savefig("fig5.png", dpi=500)
plt.show()
