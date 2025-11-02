# -*- coding: utf-8 -*-
"""
IB1020 Programmering for beregning

Forelesning om filer
"""

#%%
import random as ra
import numpy as np

throws = []
sum = 0

while sum < 50:
    this_throw = ra.randint(1,6)
    #print(this_throw)
    sum += this_throw
    throws.append(this_throw)

print("summen er", sum)
print(throws)

#file_name = "C:/Users/joakimb/OneDrive - USN/hibu/undervisning/IB1020/23/forelesning/datafiler/dice.txt"
file_name = "datafiler/dice.txt"
np.savetxt(file_name, throws, fmt='%d')

#%%
file_name = "C:/Users/joakimb/OneDrive - USN/hibu/undervisning/IB1020/23/forelesning/datafiler/dice.txt"
a = np.loadtxt(file_name)
print(a)

#%%

file_name = "C:/Users/joakimb/OneDrive - USN/hibu/undervisning/IB1020/23/forelesning/datafiler/airtravel.csv"
a = np.loadtxt(file_name, delimiter=',')
print(a)

a = a*1000
print(a)

out_file_name = "datafiler/airtravel2.csv"
np.savetxt(out_file_name, a, delimiter=',', fmt='%d')

out_file_name = "C:/Users/joakimb/OneDrive - USN/hibu/undervisning/IB1020/23/forelesning/datafiler/airtravel3.csv"
np.savetxt(out_file_name, a, delimiter=',', fmt='%.2e')

#%%

import pandas as pd

file_name = "datafiler/fiskekonkuranse.xlsx"
data = pd.read_excel(file_name)

le = data['Lars Erik'].values
print(le)
m = data['Marius'].values
j = data['Joakim'].values
print(j)

le = le[~np.isnan(le)]
m = m[~np.isnan(m)]
j = j[~np.isnan(j)]
print(j)

le_avg = np.average(le)
m_avg = np.average(m)
j_avg = np.average(j)

print("Snitt LE", le_avg)
print("Snitt M", m_avg)
print("Snitt J", j_avg)

data_dict ={
    'Lars Erik': np.array([le_avg]),
    'Marius': np.array([m_avg]),
    'Joakim': np.array([j_avg])
    }

print(data_dict)
data_out = pd.DataFrame(data_dict)
data_out.to_excel("datafiler/resultat.xlsx")

#%%
import pandas as pd
s1 = pd.Series([1,2,3,4], name='A')
s2 = pd.Series([5,6,7,8], name='B')

my_frame = pd.concat([s1, s2], axis=0)
my_frame2 = pd.concat([s1, s2], axis=1)

my_frame2['Sum'] = my_frame2.A + my_frame2.B
my_frame2['Prod'] = my_frame2.A * my_frame2.B

my_frame3 = my_frame2.iloc[:, [1,2]]
my_frame4 = my_frame2.iloc[1:3, [2,3]]

mc = my_frame2.mean(axis = 0)
print(mc)

mr = my_frame2.mean(axis=1)
print(mr)

my_frame2.to_excel("datafiler/aogb.xlsx")











