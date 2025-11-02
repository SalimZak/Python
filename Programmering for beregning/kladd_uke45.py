
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**3 + 2*x**2 - x - 2


x = 0 

while f(x) < 0:
    
    x += 0.001
    
print("Løsningen er:", round(x, 2) )     


x_val = np.linspace(0, 3, 1000)
plt.plot(x_val, f(x_val))
plt.grid()

#%%

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.log(x)

def g(x):
    return -x 

x = 0.01

while f(x) < g(x):
    
    x += 0.001
    
print("Løsningen er:", round(x, 4) )    

x_val = np.linspace(0.01, 1)
plt.plot(x_val, f(x_val), x_val, g(x_val))
plt.grid()

#%%
import numpy as np

def f(x):
       
    return x**3 + 2*x**2 - x - 2

    
x = np.linspace(-3, 3, 1000)

for i in range(0, len(x)-1):
    
    if (f(x[i]) <= 0 and f(x[i+1]) > 0 ):
        x_sol = (x[i] + x[i+1])/2
        print("Løsningen er", round(x_sol, 2)) 
        
    elif (f(x[i]) >= 0 and f(x[i+1]) < 0 ):
         x_sol = (x[i] + x[i+1])/2
         print("Løsningen er", round(x_sol, 2)) 
             
    
#%%


import numpy as np

def produkt(a, b):
    return a*b


a = np.linspace(0, 7, 100000)
prod_opt = 0
a_opt = 0
b_opt = 0


for a_val in a:
    
    b_val = 7 - a_val
    prod = produkt(a_val, b_val)
    #print(round(a_val,2), round(b_val,2) , round(prod, 2))
    if prod > prod_opt:
        prod_opt = prod
        a_opt = a_val
        b_opt = b_val

print("Optimale valg er, a=", round(a_opt, 3)," og b=", round(b_opt, 3) )


#%%


import numpy as np

a = np.linspace(0, 2, 5)

a1 = np.arange(0, 2, 0.5)


































