#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:03:59 2018

@author: sinsakuokazaki
"""
#create file
outfile = open("test.txt", "w")
outfile.write("morning\n")
outfile.write("evening\n")
outfile.write("midnight\n")
outfile.write("afternoon\n")
outfile.close()

#input filename, old string, and new string
filename = input("Enter a filename: ")
oldString = input("Enter the old string to be replaced: ")
newString = input("Enter the new string to replace the old string: ")
#read the file
infile = open(filename, "r")
newText=infile.read()

while oldString in newText:
    newText = newText.replace(oldString, newString)
infile.close()

outfile = open(filename, "w")
outfile.write(newText)


outfile.close()