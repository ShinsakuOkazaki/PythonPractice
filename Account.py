#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 00:22:23 2018

@author: sinsakuokazaki
"""

class Account:
    def __init__(self):
        self.__id = 0
        self.__balance = 100
        self.__annualInterestRate = 0
        
    def setValuable(self, id, balance, annualInterestRate):
        self.__id =id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
    
    def getID(self):
        return self.__id
    
    def getBalance(self):
        return self.__balance
    
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
    def getMonthlyInterestRate(self):
        return (self.__annualInterestRate / 100) / 12
    
    def getMonthlyInterest(self):
        return self.__balance * (self.__annualInterestRate /100) / 12
    
    def withdraw(self, amount):
        self.__balance = self.__balance - amount
    
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        
def main():
    account = Account()

    account.setValuable(1122, 20000, 4.5)
    
    id = account.getID()
    balance = account.getBalance()
    
    account.withdraw(2500)
    
    account.deposit(3000)

    print("ID is: ", id, "\nBalance is: ¥", balance, \
          "\nMonthly interest rate is: ", 100 * account.getMonthlyInterestRate(), "%", \
          "\nMonthly interest is: ¥", round(account.getMonthlyInterest(), 2))
        
main()
    