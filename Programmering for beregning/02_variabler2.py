# -*- coding: utf-8 -*-
"""
Forelesning 2
Variabler og datatyper 2
28/8-23
"""

"""
Litt repetisjon
"""
mitt_heltall = 64
print(mitt_heltall)

mitt_desimaltall = 3.1415
print(mitt_desimaltall)

min_tekst = "God dag"
print(min_tekst)

min_sannhetsverdi = True
print(min_sannhetsverdi)

min_liste = [2,4,5,7]
print(min_liste)

#%%
"""
Tupler ligner lister, 
men kan ikke endre verdi på enkeltelementer
lages med parenteser
"""
tuppel_1 = (2,4,5,3) #lager en tuppel med verdiene 2, 3, 4 og 5
print(tuppel_1)

print(tuppel_1[2])#vi kan få tak i enkeltelementer med []
#tuppel_1[2] = 6

tuppel_2 = 4,7,5
print(tuppel_2)

tuppel_3 = tuppel_1 + tuppel_2 #skjøter sammen to tupler
print(tuppel_3)

tuppel_4 = tuppel_2 * 3 #gir hele t4 3 ganger etter hverandre 
print(tuppel_4)

tuppel_4 = 1,2,3 
print(tuppel_4)

#%%
"""
Dictionary er en datatype som ligner lister
I lister bruker vi indeksen for å få tak i elementer
I dictonary bruker vi en nøkkel
"""
bil = {
       'merke': 'Ford',
       'modell': 'Fiesta',
       'år': 2021
       } #Lager en dictonary med tre nøkler og tre verdier

print(bil) #Skriver ut hele dictionaryen
print(bil['merke']) #Skriver ut verdien til merke. Det er Ford 
print(bil['modell'])

bil['reg_nr'] = 'AA13258' #legger til nøklen reg_nr med verdien AA12358
print(bil)

bil['år'] = 2023  #endrer verdien som hører til nøkkelen år
bil['år'] = bil['år'] + 1
print(bil)

#bytter merke og modell på bilen
bil['merke'] = 'BMW'
bil['modell'] = 'IX'
print(bil)

#Vi kan bruke en liste til å lagre bilen
bil_som_liste = ['BMW', 'IX', 2024, 'AA12358']
print(bil_som_liste[2]) #men da må vi huske rekkefølgen ting er lagret i

#%%
"""
Array lingner på lister, 
men har mange flere matematiske funksjoner
ligger i pakken numpy
"""
import numpy as np #importerer pakken numpy og velger å kalle den np

#Vi kan lage en array av en liste ved å bruke flere steg
liste_1 = [1,2,3,4,5] #Vi lager først en liste og lagrer den i en variabel
arr_1 = np.array(liste_1) #Så kan vi lage et array av listen

print(liste_1)
print(arr_1)

print(arr_1[2]) #vi kan få tak i enkeltelementer med []

arr_2 = np.array([6,7,8,9]) #lager en array av en liste på en linje
print(arr_2)

arr_3 = np.zeros(12) #lager et array med 12 nullere
print(arr_3)

arr_4 = np.ones(10) #lager en liste med 10 enere
print(arr_4)

#arr_5 = np.twos(6)

#%%
#Vi lager en liste og et array. Begge med verdiene 1,2,3
l1 = [1,2,3]
a1 = np.array(l1)
print("l1=", l1)
print("a1=", a1)

"""
Når vi ganger en liste med 4 får vi samme listen 4 ganger etterhverandre
l1 * 4 blir listen [1,2,3,1,2,3,1,2,3,1,2,3]
Når vi ganger et array med 4 vil alle elementene ganges med 4
a1 * 4 blir [4,8,16]
"""
l2 = l1 * 4
a2 = a1 * 4
print("l2=", l2)
print("a2=", a2)

"""
en liste + et tall er ikke lov, men vi kan si
l1 + [10] da vil 10 legges inn bakerst i l1
a1 + 10 vil øke verdien av alle elementene med 10
"""
l3 = l1 + [10]
a3 = a1 + 10
print("l3=", l3)
print("a3=", a3)

#toere = np.zeros(8)
#toere = toere + 2
#toere = np.zeros(8)+2
toere = np.ones(8)*2 #lager et array med 5 toere
print(toere)


"""
På linja under lager vi først en liste med 1 femmer.
Så ganger vi den med 12 og får en liste med 12 femmere.
Så konverterer vi lista med 12 femmere til et array
"""
femmere = np.array([5.0]*12)
print(femmere)

"""
lager et array med 11 elemnter jevt fordelt mellom 1.0 og 2.0
endepunktene blir med i arrayet
"""
en_til_to = np.linspace(1.0, 2.0, 11)
print(en_til_to)

"""
Lager et array med verdier fra 1.0 til 2.0
Hver verdi er 0.1 større enn den forrige
1.0 blir med, men 2.0 blir ikke med 
"""
arr = np.arange(1.0, 2.0, 0.1)
print(arr)

#%%
import numpy as np

#finner indeksen til minste element med argmin
arr_tilfeldig = np.array([2.86, -3.44, 11.98, 6.25])
minimum_index = np.argmin(arr_tilfeldig)
print("Det minste tallet ligger på index", minimum_index)
print("Det minste tallet er", arr_tilfeldig[minimum_index])

#finner indeksen til største element med argmax
maximum_index = np.argmax(arr_tilfeldig)
print("Det største tallet ligger på index", maximum_index)
print("Det største tallet er", arr_tilfeldig[maximum_index])

#%%
#lager et todimensjonalt array med 3 rader og 3 kolonner
arr2D = np.array([[10,20,30], [40,50,60], [70,80,90]])
print(arr2D)
print(arr2D[0])#skriver ut rad nummer 0
print(arr2D[0][2])#skriver ut elementet i rad 0 kolonne 2
print(arr2D[0,2])#skriver ut elementet i rad 0 kolonne 2

arr2D[0][2] = 6;







































