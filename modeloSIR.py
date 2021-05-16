from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def dU_dt(U, t):
    #      |         S          |                I                 |      R     |
    return [-alpha * U[0] * U[1], alpha * U[0] * U[1] - beta * U[1], beta * U[1]]

U0 = [3000000, 1, 0]
alpha, beta = 0.019, 0.1 
ts = np.arange(0, 280.32, 1.4)
Us = odeint(dU_dt, U0, ts)

S, I, R = Us[:,0], Us[:,1], Us[:,2]

fig = plt.subplots(figsize = (20,10), dpi = 80)
plt.plot(ts, S, label = 'Suscetiveis')
plt.plot(ts, I, label = 'Infectados')
plt.plot(ts, R, label = 'Retirados')
plt.ylim([0, 3000000])
plt.xlim([0, 200])

plt.legend(fontsize = 15)
plt.savefig('grafico.png')