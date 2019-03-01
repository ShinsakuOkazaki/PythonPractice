#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:33:01 2018

@author: sinsakuokazaki
"""
class Account:
    def __init__(self):
        self.__id = 0
        self.__balance = 100
        self.__annualInterestRate = 0
        
    def setID(self, id):
        self.__id = id
    
    def setBalance(self, balance):
        self.__balance = balance
        
    def setAnnualInterestRate(self, annualInterestRate):
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
    idList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    accounts = []
    for i in range(len(idList)):
        account = Account()
        account.setID(i)
        accounts.append(account)
        stop = False
    while not stop:
        inputId = int(input("Enter an account id: "))
        while inputId in idList:
            print("\nMain menu")
            print("1: check balance")
            print("2: withdraw")
            print("3: deposit")
            print("4: exit")
            
            choiceInput = int(input("Enter a choice: "))
            if choiceInput == 1:
                print("The balance is ",accounts[inputId].getBalance())
                continue
                
            elif choiceInput == 2:
                amountToWithdraw = float(input("Enter an amount to withdraw: "))
                accounts[inputId].withdraw(amountToWithdraw)
                continue
            
            elif choiceInput == 3:
                amountToDeposit = float(input("Enter an amount to deposit: "))
                accounts[inputId].deposit(amountToDeposit)
                continue
            
            elif choiceInput == 4:
                break
        
                
    
            
        
main()
    