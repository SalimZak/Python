
for i in range(5):
    print(i)

#%%    
tall = 0
while(tall <= 5):
    print(tall)
    tall += 1
    print("Hei") 
    
 
 #%%   
 
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 10*x + 20

def g(x):
    return x**2

x = np.linspace(10, 13, 100)
plt.plot(x, f(x), x, g(x))


x_coor = 0

while(g(x_coor) < f(x_coor)):
    x_coor += 0.001
 
print("Løsningen er x=", x_coor) 
 
 
#%%

tall = 30

if tall < 40:
    tall += 1
    print(tall)

while(tall < 40):
    tall += 1
    print(tall)
     
#%%

import random as ra

antall_seksere = 0
terninger = []
antall_kast = 0

while antall_seksere < 2:
    kast = ra.randint(1, 6)
    antall_kast += 1
    terninger.append(kast)
    if kast == 6:
        antall_seksere += 1
 
print(terninger, "Antall kast var:", antall_kast) 
 
#%%

pi_val = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4]


svar = True
antall_rett = 0

while svar:
        
    siffer = int(input("Skriv inn neste siffer i pi: "))
    if siffer == pi_val[antall_rett]:
        print("Riktig")
        antall_rett += 1
    
    else:
        print("Feil")
        svar = False 

print("Taltalt oppnådde du", antall_rett, "riktige siffer")

#%%

n = 28
summen = 0

for i in range(1, n+1):
    summen += 2**i

print(summen)

#%%

summen = 0
n = 0

while summen <= 8000:
    n += 1
    summen += 2**n

print(summen, n)



































 
 
 
 
 
 
 
 
 
 
 
 
 
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 