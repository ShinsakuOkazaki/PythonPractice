#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:54:29 2018

@author: sinsakuokazaki
"""

class InvalidInterestRateException(RuntimeError):
    
    def __init__(self, annualInterestRate):
        super().__init__()
        self.annualInterestRate = annualInterestRate
        
        
class InvalidWithdrawAmountException(RuntimeError):
    
    def __init__(self, amount):
        super().__init__()
        self.amount = amount
        
class InvalidDepositAmountException(RuntimeError):
    
    def __init__(self, amount):
        super().__init__()
        self.amount = amount