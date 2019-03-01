#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:19:16 2018

@author: sinsakuokazaki
"""

from time import time 

class StopWatch:
    
    def __init__(self):
        self.__startTime = time()
        self.__endTime = time()
    
    def getStartTime(self):
        return self.__startTime
    
    def getEndTime(self):
        return self.__endTime
    
    def setStartTime(self,startTime):
        self.__startTime = startTime
    
    def setEndTime(self, endTime):
        self.__endTime = endTime
        
    def start(self):
        self.__startTime = time()
        
    def stop(self):
        self.__endTime = time()
        
    def getElapsedTime(self):
        return round(self.__endTime - self.__startTime, 3)
    
def main():
    watch = StopWatch()
    total = 0
    watch.start()
    for i in range(1, 1000001):
        total += i
    watch.stop()
    print(watch.getElapsedTime())
    
main()