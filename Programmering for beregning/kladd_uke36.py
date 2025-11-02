
def f(x):
   funk = x**2 + 3*x
   return funk


def g(x):
    svar = 2*x - 1
    return svar


x_val = 0.0
f_val = f(x_val)

print("input x=", x_val, "gir output f(x)=", f_val)

g_val = g(x_val)
print("input x=", x_val, "gir output g(x)=", g_val)

#%%

def tms_til_sek(timer, minutter, sekunder):
    svar = timer*60*60 + minutter*60 + sekunder
    return svar


t = 3
m = 42
s = 50


resultat = tms_til_sek(t, m, s)

print("Resultatet er", resultat)
 



def tms_til_sek1(tiden):
    svar = tiden[0]*60*60 + tiden[1]*60 + tiden[2]
    return svar


t = 3
m = 42
s = 50

tid = [t, m, s]

resultat = tms_til_sek1(tid)

print("Resultatet er", resultat)
 
#%%

import numpy as np

def rektangel(lengde, bredde):
    ar = lengde*bredde
    omk = 2*lengde + 2*bredde
    diag = np.sqrt(lengde**2 + bredde**2 )
    return ar, omk, diag


l = 3.0
b = 4.0

areal, omkrets, diagonal = rektangel(l,b)

print("Areal:", areal, "Omkrets:", omkrets, "diagonal:", diagonal) 

   
    




































