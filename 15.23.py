#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 00:09:26 2018

@author: sinsakuokazaki
"""

def displayPermuation(s):
    s = list(s)
    displayPermuationHelper(s, 0, len(s)-1)
    
def displayPermuationHelper(s, s1, s2):
    if s1 == s2:
        st = ''.join(s)
        print(st)
    
    else: 
        for i in range(s1, s2 + 1):
            s[s1], s[i] = s[i], s[s1]
            displayPermuationHelper(s, s1 + 1, s2)
            s[s1], s[i] = s[i], s[s1]
            
            
def main():
    strInput = input("Enter a string: ")
    print("The permuations are: ")
    displayPermuation(strInput)
            

main()