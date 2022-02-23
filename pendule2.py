import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt

g = 9.81
l = 0.01

tau = np.sqrt(l/g)

def f(t, y):
    theta = y[0]
    omega = y[1]
    return [omega, -1/tau**2*np.sin(theta)]

def linear(t, theta0):
    return theta0*np.cos(t/tau)

begins = [np.pi/20, np.pi/6, np.pi/3, np.pi/2]
labels = [r"$Condition\/initiale : \frac{\pi}{20}$", r"$Condition\/initiale : \frac{\pi}{6}$", r"$Condition\/initiale : \frac{\pi}{3}$", r"$Condition\/initiale : \frac{\pi}{2}$"]
end = 3*2*np.pi*tau
results = [scipy.integrate.solve_ivp(f, [0,end], [begin, 0], t_eval=np.linspace(0,end,1000)) for begin in begins]

plt.figure(figsize=(10,10))


i=0
for r in results:
    plt.subplot(2,len(results)//2,i+1)
    plt.plot(r.t, r.y[0])
    plt.plot(r.t, [linear(t, begins[i]) for t in r.t])
    plt.legend(["Non-linéaire", "Linéarisée"], loc="lower right")
    plt.title(labels[i])
    plt.xlabel("Temps (s)")
    plt.ylabel(r"$\theta$")
    plt.axis()
    i+=1

plt.show()
# plt.savefig("pendule.png")