#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 22:32:42 2018

@author: sinsakuokazaki
"""
#import csv
import csv
#open file to read
infile = open("sample_input_charles_dickens.txt", "r")
a = 0
aUpper = 0
b = 0
bUpper = 0
total = 0
#count a, A, b, B, and non-alphabetic string
for line in infile:
    a += line.count("a")
    aUpper += line.count("A")
    b += line.count("b")
    bUpper += line.count("B")
    for char in line:
        if char.isalpha():
            total += 1
infile.close()

#calculate parcentage 
aRate = round(((a + aUpper) / total * 100), 2)
bRate = round(((b + bUpper) / total * 100), 2)

#creat data to write
data = [["Char", "Freq", "%total"], ["A", a + aUpper, aRate], ["B", b + bUpper, bRate]]

#write data in csv
outfile = open("charles_dicken.csv", "w")
writer = csv.writer(outfile)
writer.writerows(data)

outfile.close()