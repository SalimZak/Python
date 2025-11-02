
# Case1

import numpy as np

def pannekaker( ant ):
    
    #enhet = np.array(["dl mel", "dl melk", "antall egg", "ss smør", "ts salt"])
    oppskrift = np.array([3, 6, 4, 2, 0.5])
    
    oppskrift = ant*oppskrift/12
    
    oppskrift[2] = round(oppskrift[2])
    
    if ( ant == 1):
        
        oppskrift[2] = 1
        
    return oppskrift    
    

antall = 14

enhet = np.array(["dl mel", "dl melk", "antall egg", "ss smør", "ts salt"])
    
skalert_oppskrift = pannekaker(antall)
#print(skalert_oppskrift, enhet)

for i in range(0, len(skalert_oppskrift)):
    
    print(round(skalert_oppskrift[i], 2), enhet[i])
    
#%%

#Case 2

import numpy as np

def minste_sylinder(l, b, h):
    
    hs = 10
    r = 0.1 
    vol_boks = l*b*h
    vol_syl = np.pi*r*r*hs 
    
    while (vol_syl < vol_boks):
        r += 0.1
        vol_syl = np.pi*r*r*hs
    
    print("Minste radius er:", r)
        
lengde = 8
bredde = 6
h_boks = 16

minste_sylinder(lengde, bredde, h_boks)

#%%

#Case 5
# se alternativ kode litt lenger ned (men denne er som på foilene)
import numpy as np


def fjern_element(arr, k):
    
    liste = np.arange(k-1, len(arr)-1)
    arr = np.delete(arr, liste)
    return arr 

    
arr1 = np.random.randint(0, 11, 10)
k_val = 6

print(arr1)
new_arr = fjern_element(arr1, k_val)
print(new_arr)

#%%

#Case 5
#Alternativ kode (fra Joakim og jeg liker denne bedre enn min egen)


import numpy as np


def fjern_element(arr, k):
    
    while (len(arr) > k):
        arr = np.delete(arr, k)
    
    return arr 

    
arr1 = np.random.randint(0, 11, 10)
k_val = 6

print(arr1)
new_arr = fjern_element(arr1, k_val)
print(new_arr)































    






    