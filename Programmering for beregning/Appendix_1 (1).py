# oppgave 1a
import numpy as np

def midtpunkt(a,b):
  return (a+b)/2

# oppgvaen var litt uklar med input så jeg gjorde det på 2 måter. manuelt og gjennom python
#manuelt: jeg velger a til 4 og b til 3
svar = midtpunkt(4,3)
print("svaret er: ", svar, "a= ", a, "b= ", b)

#gjennom python er det
a = input("a sin verdi = ")
b = input ("b sin verdi er = ")
print("svaret er: ", svar, "a= ", a, "b= ", b)

# oppgave 1b
import numpy as np

def vektetpunkt(a,b,c):
  x = a*(1-c)+b*c
  c = np.linspace(0,1,100)
  if c < 0.5:
    x = a
  if c > 0.5:
    x = b
  if c == 0.5:
    a = b
  return x

# kunne satt opp med if c == 0.5, elif c > 0.5, else: den siste, med ville gjøre det mer tydelig for dere. 
svar_1_b = vektetpunkt(1,1,0)
print("a =", a, "b= ", b, "c= ", c, "svaret av funksjonen er: ", svar_1_b)

# oppgave 1c
import numpy as np

def vektetpunkt(a,b,c):
  return a*(1-c)+b*c

c = 0
n = 100
summen = 0

for c in range(1,n+1):
  summen += vektetpunkt(4,9,c)
  c += 0.01

print ("resultatet: ", summen, "hver iterasjon: ", c)

#%% oppgave 2a
import numpy as np

arr1 = np.random.rand(100)

def finnAntall(arr1):
  antall = 0
  for i in range (len(arr1)):
    while arr1[i] > 0.4 and arr1[i] < 0.5:
      antall += 1
  return antall

print ("hvor mange av tallene ligger i intervallet: ", antall)

# oppgve 2b

import numpy as np

arr1 = np.random.rand(100)

def finnIndex(arr1):
  n = 0
  svar_2_b = 0
  for i in range (len(arr1)):
    if arr1[i] > arr1[i+1]:
      svar_2_b = arr1[n]
      n += 1
  return svar_2_b
  
print("hver element som er større:", svar_2_b)

#oppgave 2c
import numpy as np

arr1 = np.random.rand(100)

def finnAntallElement(arr1):
  summen = 0
  antallet = 0
  for i in range(len(arr1)):
    while summen >= 25:
      arr1[i] += antallet
      antallet += 1
  return antallet

print("antall elementer som inngikk", antallet)

#%% oppgave 3
import numpy as np

deltagere = 3*["F"]+19*["L"]

n = 1000
gunstige = 0

for i in range (n):
  svar = np.random.choice(deltagere, 3, False)
  if (svar[0] and svar[1] == "L"):
    gunstige += 1

print("sansynligheten er: ", gunstige/n,2)

#%% oppgave 4
import numpy as np

def h_siden(h,R):
  return np.sqrt(4*(2*h*R-h**2))

R = 123.9
K = 135
h = 0
    
if K <= h_siden(h,R):
  h += 0.1

print("svaret til høyre siden nå er:", h_siden, "høyden er: ", h)






