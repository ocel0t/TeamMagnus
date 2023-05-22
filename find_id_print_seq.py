# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:09:42 2023

@author: ocel0t
"""

import linecache

file_id='C:\\Users\\ocel0t\\OneDrive - Umeå universitet\\NTM\\egyetem\\scriptek\\NTM\\python\\ids.txt'
file_seq='C:\\Users\\ocel0t\\OneDrive - Umeå universitet\\NTM\\egyetem\\scriptek\\NTM\\python\\seq.fa'

with open(file_id, 'r') as file:
    ids = [line.split()[0] for line in file]
    
ids2=[]    
for i in ids:
    ids2.append(str('>' + i[:-2])) 
    
with open(file_seq, 'r') as file2:
    seq = [line.split()[0] for line in file2]

noLines=0
for i in ids2:
    for e in seq:
        if i==e:
            line = linecache.getline(file_seq, noLines+2)
            print(i)
            print(line)
            with open('results.txt', 'a') as file3:
                file3.write(i + '\n')
                file3.write(line)     
        noLines+=1    
        line=""
    noLines=0