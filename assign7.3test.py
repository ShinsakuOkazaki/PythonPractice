#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 01:03:44 2018

@author: sinsakuokazaki
"""

from Account import Account

account = Account(1122, 20000, 4.5)

account.withdraw(2500)

account.deposit(3000)

print("ID is: ", account.id, "\nBalance is: ¥", account.balance, \
      "\nMonthly interest rate is: ", 100 * account.getMonthlyInterestRate(), "%", \
      "\nMonthly interest is: ¥", round(account.getMonthlyInterest(), 2))