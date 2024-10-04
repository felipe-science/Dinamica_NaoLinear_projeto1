from numpy import linspace, exp, log
import pylab as plt

def functionV(K, V0, r, t0):

    listK = []
    listV = []
    listt = linspace(0,5,100)
    for t in listt:
        V = K*exp(log(V0/K)*exp(-r*(t-t0)))
        listV.append(V)
        listK.append(10)

    return listt, listV, listK


r = 1.5
K = 10.0
V0 = 0.01
t0 = 0.0


listt, listV, listK = functionV(K,V0,r,t0)

plt.plot(listt, listV, color='blue')
plt.plot(listt, listK, '--', color = 'red')
plt.gca().set_xticks([])
plt.gca().set_yticks([])
plt.xlabel("Tempo", fontsize='20')
plt.ylabel("Volume", fontsize='20')
plt.xlim(0,5)

plt.text(-0.25, V0, r'$V_{0}$', fontsize=12, color='black')
plt.text(-0.2, 9.9, r'$K$', fontsize=12, color='black')
plt.savefig("analitical.png")
plt.show()