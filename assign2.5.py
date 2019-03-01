#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:58:59 2018

@author: sinsakuokazaki
"""

#input subtotal and a gratuity rate
subtotalInput, gratuityRateInput = input("Enter the subtotal and a gratuity rate: ").split(", ")

#convert input string into float
subtotal, gratuityRate = float(subtotalInput), float(gratuityRateInput)

#calculate gratuity
gratuity = subtotal * gratuityRate / 100

#calculate total
total = subtotal + gratuity

#print result
print("The gratuity is", round(gratuity, 2), " and the total is", round(total, 2))