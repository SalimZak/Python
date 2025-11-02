#%% oppgave 1A

import numpy as np
def omkrets(r, l):
  return 2*np.sqrt(l**2+r**2)+np.pi*r
def areal(r,l):
  return np.pi*r**2/2+l*r

rad = 30
for i in range(40,85,2):
  i+= 1
omk = omkrets(rad,i)
ar = areal(rad,i)
  
print("verdi", l, "omkrets", omk, "areal", ar)
#%%
import numpy as np
import matplotlib.pyplot as plt
def omkrets(r,l):
  l=30
  r=np.linspace(25,35,10000)
  return 2*np.sqrt(l**2+r**2)+np.pi*r

plt.plot(omkrets(r),omkrets(l))
plt.grid()
#%% oppgave 2
import numpy as np

arr100= np.zeros(100)
n = 1
sum = 0
sum1 = 0
sum2 = 0
for i in range(0,101):
  b = n/i
  i += 1
  sum += b
  while sum >= 4
    print ("sum",sum, "antall", b)
  if (i < 7):
    i += 1
    b = n/i
    sum1 += b
    print("Summen fra og med index 0 til og med index 7 er størst",sum1)
    else{
      sum2 += b
      print("Summen fra og med index 8 til og med index 99 er størst", sum2)
    }
#%% oppgave 3
import numpy as np

sample_space = np.array(["h", "u", "b"])
prob = [0.5,0.2,0.3]
gunstige = 0
n = 100

for i in range (0,n):
  resultat = np.random.choice(sample_space,5,prob)
  i += 1
  if (resultat[3] == "u" and resultat[5] == "b" or "u")
    gunstige += 1

print("sansnligheten er ", gunstige/n)

#%% oppgave 4
import numpy as np

omkrets = 400
bra_l = 0
bra_r= 0
best_o = 0

om = 2*np.pi*r + 2*l
for i in range(1,om):
  i += 0.1
  areal = 2*r*om
  best_o += 1

if areal > best_o:
  best_o = areal
  bra_r = r
  bra_l = l
  
print( best_o)


    

  


