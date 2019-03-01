#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:37:52 2018

@author: sinsakuokazaki
"""
#input numbers separated by space
l = input("Enter ten numbers: ")
#convert the string to list sprited by space
strList1 = l.split(" ")
#change the elements of list to integer
list1 = [ int(i) for i in strList1]
#copy the elements in list1 to list2 if list2 does not have the same element
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
#sort the elements in list2, convert the integer elements in list2 to string elements
answer = " ".join([str(i) for i in sorted(list2)])
print("The distinct numbers are: ", answer)
