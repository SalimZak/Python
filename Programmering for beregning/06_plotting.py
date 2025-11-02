# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np

x_vals = np.array([20, 30, 50])
y_vals = np.array([2, 2.5, 3])

plt.figure(1)
plt.plot(x_vals, y_vals)
plt.show()

x_vals2 = np.array([1,2,3])
y_vals2 = np.array([6,4,3])

plt.figure(2)
plt.plot(x_vals, y_vals)
plt.plot(x_vals2, y_vals2)

plt.figure(3)
plt.subplot(2,1,1)
plt.plot(x_vals, y_vals)
plt.subplot(2,1,2)
plt.plot(x_vals2, y_vals2)

#%%
plt.figure(4)
plt.subplot(2,2,1)
plt.plot(x_vals, y_vals, 'r')
plt.subplot(2,2,2)
plt.plot(x_vals2, y_vals2, 'b')
plt.subplot(2,2,3)
plt.plot(x_vals, y_vals2, 'y')
plt.subplot(2,2,4)
plt.plot(x_vals2, y_vals, 'g')

#%%

plt.figure(5)
plt.subplot(2,1,1)
plt.plot(x_vals, y_vals, '*:k')
plt.subplot(2,1,2)
plt.plot(x_vals2, y_vals2, '-..g')

#%%
mnd = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
kr = np.array([231,5478,4355, 4376, 8765, 5565, 7999, 3333, 6666, 7654, 3443, 5358])

plt.figure(6)
plt.xlabel('Måned')
plt.ylabel('Saldo')
plt.title('Min Formue i 2022')
plt.axis([0, 13, -500, 10000])
plt.grid()
plt.plot(mnd, kr, 'o--c')


#%%
def f(x):
    ans = np.sqrt(x)
    return ans

def g(x):
    ans = x
    return ans

def h(x):
    ans = x**2
    return ans

x_vals3 = np.linspace(0.1, 5, 200)
y_vals3 = f(x_vals3)
y_vals4 = g(x_vals3)
y_vals5 = h(x_vals3)

plt.figure(7)
plt.plot(x_vals3, y_vals3, 'y')
plt.plot(x_vals3, y_vals4, 'r')
plt.plot(x_vals3, y_vals5, 'g')


#%%

navn = np.array(['Marius', 'Lars Erik', 'Joakim'])
ant_fisk = np.array([10, 13, 4])

plt.figure(8)
plt.xlabel("Deltager")
plt.ylabel("Antall fisk")
plt.title('Resultater fra USN-fiskekonkuransee 2023')
plt.bar(navn, ant_fisk, color=('green', 'yellow', 'red'))

#%%
#andel = ant_fisk/sum(ant_fisk)
#print(andel)

plt.figure(9)
plt.pie(ant_fisk, labels=navn)

#%%
n= 10000
x = np.random.randn(n)
bins = 200
#print(x)

plt.figure(10)
plt.hist(x, bins)






