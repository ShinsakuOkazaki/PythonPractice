#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 00:22:23 2018

@author: sinsakuokazaki
"""

class Account:
    
    def __init__(self, id = 0, balance = 100, annualInterestRate = 0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
        
    def getId(self):
        return self.__id
    
    def getBalance(self):
        return self.__balance
    
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
    def setId(self, id):
        self.__id =id
        
    def setBalance(self, balance):
        self.__balance = balance
        
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate
        
    def getMonthlyInterestRate(self):
        return (self.__annualInterestRate / 100) / 12
    
    def getMonthlyInterest(self):
        return self.__balance * (self.__annualInterestRate / 100) / 12
    
    def withdraw(self, amount):
        self.__balance = self.__balance - amount
    
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        
    
def main():
    account = Account(1122, 20000, 4.5)

    account.withdraw(2500)

    account.deposit(3000)

    print("ID is: ", account.getId(), "\nBalance is: ¥", account.getBalance(), \
          "\nMonthly interest rate is: ", 100 * account.getMonthlyInterestRate(), "%", \
          "\nMonthly interest is: ¥", round(account.getMonthlyInterest(), 2))
    
main()