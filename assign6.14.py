#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:03:59 2018

@author: sinsakuokazaki
"""

def estimatePi(i):
    s = 0
    for i in range(1, i+1):
        s += (-1)**(i + 1) / (2 * i - 1)
        
    mI = 4 * s
    return mI


print(format("i", "<15s"), end = "")
print(format("m(i)", "<6s"), end="\n\n")
for i in range(1, 902, 100):
    print(format(i, "<15d"), end ="")
    print(format(estimatePi(i), "<6.4f"))