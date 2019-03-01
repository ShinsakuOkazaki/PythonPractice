#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 17:28:11 2018

@author: sinsakuokazaki
"""
#import randint
from random import randint

#write 70 random integers between 0 and 100 in scores.txt
outfile= open("scores.txt", "w")
for i in range(70):
    outfile.write(str(randint(0, 100))+"\n")
outfile.close()

#input filename
filename = input("Enter a filename: ")

#open file to read
infile = open(filename, "r")
numbers = infile.readlines()
numberOfScores = 0
total = 0
#calculate number of scores and total
for number in numbers:
    numberOfScores += 1
    total += int(number[:2])
infile.close()

#calculate average
average = total / numberOfScores

print("There are", numberOfScores, "scores")
print("The total is", total)
print("The average is", average)