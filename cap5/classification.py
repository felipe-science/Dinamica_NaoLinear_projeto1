import numpy as np
import pylab as plt


tau = np.linspace(-1,1,1000)
delta = (tau**2)/4

xlvert = np.zeros([1000])
ylvert = np.linspace(0,0.25,1000)




plt.plot(tau,delta)
plt.plot(xlvert,ylvert)


plt.text(-1.0, 0.05, 'stable nodes', fontsize=12, color='black')
plt.text(-0.5, 0.1, 'stable spiral', fontsize=12, color='black')
plt.text(+0.05, 0.1, 'unstable spiral', fontsize=12, color='black')
plt.text(+0.5, 0.05, 'unstable nodes', fontsize=12, color='black')
plt.text(-0.143, 0.15, 'centers', fontsize=12, color='black')

plt.text(-0.98, 0.24, r'$\tau^{2} - 4\Delta = 0$', fontsize=12, color='black')
plt.text(-0.93, 0.22, r'$(b/m)^{2} = 4k/m$', fontsize=12, color='black')

ax = plt.gca()

# Removendo os rótulos dos eixos x e y
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.xlabel(r"$\tau = k/m$", fontsize='15')
plt.ylabel(r"$\Delta = k/m$", fontsize='15')

plt.savefig("classification.png", dpi=300)
plt.show()
