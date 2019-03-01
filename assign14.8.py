#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 16:40:00 2018

@author: sinsakuokazaki
"""
#aquire file name (my file name is shinsaku.txt)
file = input("Enter a file name: ")
#open the file for read
infile = open(file, "r")
#read file and store it 
readedFile = infile.read()
#close the file
infile.close()
#convert spring into list spritting by space
lst = readedFile.split()
#conver list to set to eliminate duplicated number
st = set(lst)
#convert set to list and sort it
lst2 = sorted(list(st))

print("\nNon-duplicate words are\n")
for i in lst2:
    print(i)