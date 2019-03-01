#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 22:58:10 2018

@author: sinsakuokazaki
"""

#1.11

#seconds for one year
secondsForYear = 60 * 60 * 24 * 365

#corrent population
correntPopulation = 312032486

#number of birth in one year
birthInYear = secondsForYear // 7

#number of death in one year
deathInYear = secondsForYear // 13

#number of death in one year
immigrantInYear = secondsForYear // 45

#population increasing in one year
increasedPopulation = birthInYear - deathInYear + immigrantInYear

#population in next first year
firstPopulation = correntPopulation + increasedPopulation

#population in next second year

secondPopulation = correntPopulation + 2 * increasedPopulation

#population in next third year
thirdPopulation = correntPopulation + 3 * increasedPopulation

#population in next fourth year
fourthPopulation = correntPopulation + 4 * increasedPopulation

#population in next fifth year
fifthPopulation = correntPopulation + 5 * increasedPopulation

#print each population in each year
print("The population for next first year is", firstPopulation)
print("The population for next second year is", secondPopulation)
print("The population for next third year is", thirdPopulation)
print("The population for next fourth year is", fourthPopulation)
print("The population for next fifth year is", fifthPopulation)