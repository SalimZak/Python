
import numpy as np

utfallsrom = np.array([1, 2, 3, 4, 5, 6])

sum_syv = 0
n = 10000

for k in range(0, n):
    
    terning1 = np.random.choice(utfallsrom)
    terning2 = np.random.choice(utfallsrom)
    
    if (terning1 + terning2 == 7):
        sum_syv += 1

print("Sum syv oppnås med sannsynlighet:", sum_syv/n)


#%%


import numpy as np

n = 10000
utfallsrom = np.array([1, 2, 3, 4, 5, 6])
gunstig = 0

for k in range(0, n):
    terninger = np.random.choice(utfallsrom, 3)
    
    if (np.sum(terninger) >= 9  and (2 in terninger) ):
        gunstig += 1
        
print("Svaret er", gunstig/n)        

#%%

import numpy as np


utfallsrom = np.array([1,2,3,4,5,6])
n = 10000

gunstig_utfall = 0

for p in range (0, n):
  terning1 = np.random.choice(utfallsrom)
  terning2 = np.random.choice(utfallsrom)
  terning3 = np.random.choice(utfallsrom)

  if (terning1+terning2+terning3 >= 9) and (terning1 ==2 or terning2==2 or terning3 == 2):
      gunstig_utfall += 1

print('Sansynligheten er:', gunstig_utfall/n*100,'%')


#%%

import numpy as np

utfallsrom = 105*[0]
utfallsrom[0] = "j"
utfallsrom[1] = "a"

n = 100000
gunstig = 0

for k in range(0, n):
    
    tast = np.random.choice(utfallsrom, 2)
    if(tast[0] == "j" and tast[1] == "a"):
        gunstig += 1
        
print("svaret er:", gunstig/n)        
        
    
#%%

utfallsrom = np.array(["G", "G", "G", "R", "R"])  

n = 10000
gunstig = 0

for i in range(0, n):
    
    to_kuler = np.random.choice(utfallsrom, 2, False)
    if (to_kuler[0] == "R" and to_kuler[1] == "R"):
        gunstig += 1

print("svaret er", gunstig/n)        



















        
    






































