#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 13:14:38 2018

@author: sinsakuokazaki
"""
#import random
import random
#create dictionary
state = ["Alabama", "Alaska", "Arizona"]
capital = ["Montgomery", "Juneau", "Phoenix"]
answer = dict(zip(state, capital))
#obtain list of dictionary keys
question = list(answer.keys())
#randomize the key list
random.shuffle(question)

count = 0
for i in question:
    userInput = input("What is the capital of " + i + "? ")
    if userInput.lower() == answer[i].lower():
        print("Your answer is correct")
        count += 1
    else:
        print("The correct answer should be", answer[i])

print("The correct count is", count)        