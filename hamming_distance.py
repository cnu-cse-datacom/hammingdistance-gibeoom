import random
import numpy as np
import pandas as pd
from hamming_practice import hamming

df = pd.read_csv('sample.csv',names=['word','bin'])

count = 0
min = hamming(max(df.iloc[:,1]),min(df.iloc[:,1]))
for i in range(0,len(df)-1):
    for j in range(i+1, len(df)):
        hd = hamming(df.iloc[i,1],df.iloc[j,1])
        print(count,"(",df.iloc[i,0],df.iloc[j,0],")hamming_distance:",hd)
        if(min > hd):
            min = hd
        count += 1
        
print("min hamming distance", min)
