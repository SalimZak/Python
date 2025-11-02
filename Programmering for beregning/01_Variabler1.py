# -*- coding: utf-8 -*-
"""
Forelesning 1
Variabler og datatyper 1
21/8-23
"""

#%%
print(4+5) #Her skriver svaret av 4+5

tall = 4+5 #Lager en variabel med navn tall og gir den verdien 9
print(tall) #Skriver ut verdien av tall


tall2 = tall + 2 #lager en ny variabel med navn tall2. Den får verdien 11
print(tall2)

tall = 10 #Gir variabelen tall en ny verdi
print(tall)
print(tall2)

"""
Variblelnavn kan bestå av bokstaver, tall og _
De kan ikke starte med tall
"""
asdf = 5
ASDF = 4 #Variabelen asdf er ikke den samme som ASDF. Det skilles på små og store bostaver
asdf1 = 3
#1asdf = 5 #Variabelnavn kan ikke starte med tall
AS_DF = 7

"""
Vi kan ikke bruke mellomrom i variabelnavn
bruk _ eller stor bokstav for å skille mellom ord
"""
antall_studenter_som_kan_programmere = 221
antallStudenterSomKanProgrammere = 221




print(ASDF)

print(type(tall)) #vi kan finne typen til en variabel med type()


"""
Til nå har alle variabler vært heltall altså int
Variabler av typen float kan holde desimaltall
"""
desimaltall = 4.98
print(desimaltall)

desimaltall2 = 100/3
print(desimaltall2)
print(f'{desimaltall2:.2f}') #skriver ut med 2 desimaler

stort_desimaltall = 8643563677432947.644564
print(f'{stort_desimaltall:.2e}') #skriver ut med 2 desimaler på vitenskaplig form

lite_desimaltall = 0.0000000000032592
print(f'{lite_desimaltall:.2e}')

tall3 =  desimaltall + tall

#%%

"""
String er en datatype for tekst
"""
tekst1 = 'Dette er en tekst' # en string står mellom ' ' eller " "
tekst2 = "Dette er også en tekst"

#Her kommer 2 ulike måter å skrive ut anførselstegn på
tekst3 = "Tom's cat"
tekst4 = 'Tom\'s cat'
print(tekst3)
print(tekst4)

#Vi kan skjøte sammen stringer med +
tekst5 = tekst1 + " " + tekst2
print(tekst5)


tall = 4
variabel = str(tall) #Vi konverterer fra tall til string med str()
print(variabel+variabel) #Her bruker vi string + altså tekstsammenskjøting

#%%
#input lar oss hente en string fra brukeren
alder = input("Hvor gammel er du")
print("du er", alder, 'år gammel')
print("neste år er du", int(alder) + 1, "år gammel") #vi må konvertere for å regne med svar

#%%
#boolske variabler kan ha en av to verdier, True eller False (sann eller usann)
b1 = True
print(b1)

b2 = False
print(b2)

print(b1 or b2)
print(b1 and b2)
print(not b1)

a = 4
b = 4

print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a == b)
print(a != b)

b3 = a < b


#%%
#lister lages med []
l1 = [] #her lager vi en tom liste
print(l1)
print(type(l1))

l2 = [2, 5, 3, 7, 5] #lager en liste med 5 heltall
print(l2)

l3 = [3, 7.7, "hei", True, [3,6]] #lager en liste med 5 elementer av ulik type
print(l3)

print(l3[2]) #skriver ut element på plass 2 i l3. Husk at vi begynner å telle på 0

l3[2] = "Hallo" #Bytter ut element på plass 2 i l3 med Hallo
print(l3)

var1 = l3[1]
print(var1)

var2 = l3[1:3] #lager en ny liste og gir den verdi nummer 1 og 2 fra l3
print(var2)

l3[0:3] = [100, 200, 300] # erstatter element nummer 0,1 og 2 med nye verdier
print(l3)

l3.append(9999) #legger til 9999 som nytt element bakerst i l3
print(l3)

l3.extend([11, 22, 33]) #legger inn verdiene 11, 22 og 33 bakerst i l3
print(l3)



