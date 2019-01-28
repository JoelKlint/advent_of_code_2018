import numpy as np
import datetime

data = []
with open('./input.txt', 'r') as r_file:
    data = r_file.readlines()
    data = [ d.strip() for d in data ]

min = 9999999999999999
for glob_c in 'qwertyuiopasdfghjklzxcvbnm':
    word = data[0].replace(glob_c, "").replace(glob_c.upper(), "")
    len_1 = len(word)
    len_2 = len_1+1
    while len_1 != len_2:
        len_2 = len_1
        for c in 'qwertyuiopasdfghjklzxcvbnm':
            word = word.replace(c+c.upper(), "").replace(c.upper()+c, "")
        len_1 = len(word)
    if len_1 < min:
        min = len_1

print(min)
