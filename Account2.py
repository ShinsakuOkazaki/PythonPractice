#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:35:05 2018

@author: sinsakuokazaki
"""

from AccountException import InvalidInterestRateException, InvalidWithdrawAmountException, \
                                InvalidDepositAmountException

class Account2:
    def __init__(self, id = 0, balance = 100, annualInterestRate = 0):
        self.__id = id
        self.__balance = balance
        if annualInterestRate >=0:
            self.__annualInterestRate = annualInterestRate
        else: 
            raise InvalidInterestRateException(annualInterestRate)    
        

    def setID(self, id):
        self.__id = id
    
    def setBalance(self, balance):
        self.__balance = balance
        
    def setAnnualInterestRate(self, annualInterestRate):
        if annualInterestRate >= 0:
            self.__annualInterestRate = annualInterestRate
        else:
            raise InvalidInterestRateException(annualInterestRate)
    
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
        if amount >= 0:
            self.__balance = self.__balance - amount
        else:
            raise InvalidWithdrawAmountException(amount)
    def deposit(self, amount):
        if amount >= 0:
            self.__balance = self.__balance + amount
        else:
            raise InvalidDepositAmountException(amount)
        
def main():
    try:
        account = Account2(1144, 20000, -4.5)
        
        id = account.getID()
        balance = account.getBalance()
        
        account.withdraw(200)
        account.deposit(2500)
        
        print("ID is: ", id, "\nBalance is: ¥", balance, \
          "\nMonthly interest rate is: ", 100 * account.getMonthlyInterestRate(), "%", \
          "\nMonthly interest is: ¥", round(account.getMonthlyInterest(), 2))
        
    except InvalidInterestRateException as ex:
        print("The annual interest rate", ex.annualInterestRate,"is invalid")
        
    except InvalidWithdrawAmountException as ex:
        print("The amount for withdraw", ex.amount,"is invalid")
        
    except InvalidDepositAmountException as ex:
        print("The amount for deposit", ex.amount,"is invalid")
    else:
        print("transaction succeeded")
    finally:
        print("Finish!!")
        
main()