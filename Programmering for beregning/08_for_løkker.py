# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:34:16 2023

@author: joakimb
"""

temperaturer = [1.4, 6.3, -3.8, 1.9, -4.6, -5.3, 2.9, 4.6]

#print(temperaturer[0])
#print(temperaturer[1])

for temp in temperaturer:
    print(temp)
    
antall_positive = 0
antall_negative = 0

for temp in temperaturer:
    if temp < 0:
        antall_negative += 1
    else:
        antall_positive += 1
        
print("antall negative", antall_negative, "Antall positive", antall_positive)

#%%

for i in range(1,21):
    print(i)
#%%

for i in range(0, 31, 3):
    print(i)

#%%
#oppgave: summer alle tallene mellom 2 og 24

sum = 0
for i in range(2, 25, 1):
    #print(i)
    sum += i

print("Summen er", sum)

#%%
#regn ut summen av tallene 5**2 + 6**2 + 7**2 + ... 50**2

sum = 0
for i in range(5, 51):
    print(i)
    sum = sum + i**2
    
print("summen er", sum)

#%%
#regn ut summen av alle tallene mellom 0 og 100 som er delelig med 4

#for i in range(0, 101, 4):
#    print(i)

sum = 0    
for i in range(0, 101):
    if i%4 == 0:
        sum += i

print("summen er", sum )


#%%
# finn ut når to grafer krysser hverandre (f(x) = g(x))

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*x - 3

def g(x):
    return -x**2 + 2*x + 1

x_vals = np.linspace(-1, 3, 10000)

plt.figure(1)
plt.plot(x_vals, f(x_vals), 'g')
plt.plot(x_vals, g(x_vals), 'b')
plt.grid()

#beste_x = np.inf
beste_x = x_vals[0]

for x in x_vals:
    if g(x) >= f(x):
        beste_x = x

print("f(x) = g(x) når x =", beste_x)


#%%
#sprettball

h_start = 1.5
faktor = 0.9
antall_sprett = 49

avstand = h_start
for i in range(1, antall_sprett+1):
    #print(i)
    avstand = avstand + 2*(h_start * faktor**i)
    
print("Den totale avstanden er", round(avstand, 2), "meter")


#%%
#skriv ut den lille gangetabellen

for x in range(0, 11):
    for y in range(0,11):
        print(x, "*", y, "=", x*y)

print("Det var hele gangetabellen")























