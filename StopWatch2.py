#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 16:26:05 2018

@author: sinsakuokazaki
"""

from time import time 

class StopWatch2:
    
    def __init__(self):
        self.__startTime = 0
        self.__endTime = 0
        self.__initialState = True
        self.__runningState = False
        self.__stopState = False
    
    def getStartTime(self):
        return self.__startTime
    
    def getEndTime(self):
        return self.__endTime
    
    def getState(self):
        if self.__initialState:
            return "initial state"
        elif self.__runningState:
            return "running state"
        elif self.__stopState:
            return "stop state"
    
    def setStartTime(self,startTime):
        self.__startTime = startTime
    
    def setEndTime(self, endTime):
        self.__endTime = endTime
        
    def start(self):
        if self.__startTime == 0:
            self.__startTime = time()
        self.__initialState = False
        self.__runningState  = True
        self.__stopState = False
        
    def stop(self):
        self.__endTime = time()
        self.__initialState = False
        self.__runningState  = False
        self.__stopState = True
        
    def getElapsedTime(self):
        if self.__initialState == True:
            return 0
        
        elif self.__runningState == True:
                
            return round(time() - self.__startTime, 3)
        
        elif self.__stopState == True:
            return round(self.__endTime - self.__startTime, 3)
        
    def reset(self):
        self.__initialState = True
        self.__runingState  = False
        self.__stopState = False
        
        
        
        
        
def main():
    watch = StopWatch2()
    total = 0
    watch.start()
    for i in range(1, 1000001):
        total += i
        
    print("Elapsed time:",watch.getElapsedTime(),\
          "\nState:", watch.getState(),"\nStart time:", watch.getStartTime(),\
          "\nEnd time:", watch.getEndTime(), end = "\n\n")
    
    for i in range(1, 1000001):
        total += i
    
    watch.stop()
    print("Elapsed time is", watch.getElapsedTime(),\
          "\nState:", watch.getState(), "\nStart time:", watch.getStartTime(),\
          "\nEnd time:", watch.getEndTime(), end = "\n\n")
    
    for i in range(1, 1000001):
        total += i
    
    watch.stop()
    print("Elapsed time is",watch.getElapsedTime(),\
          "\nState:", watch.getState(), "\nStart time:", watch.getStartTime(),\
          "\nEnd time:", watch.getEndTime(), end = "\n\n")
    
    watch.reset()
    print("Elapsed time is reset to", watch.getElapsedTime(),\
          "\nState:", watch.getState(), "\nStart time:", watch.getStartTime(),\
          "\nEnd time:", watch.getEndTime(), end = "\n\n")
    
    watch.start()
    for i in range(1, 1000001):
        total += i
    
    print("Elapsed time:",watch.getElapsedTime(),\
          "\nState:", watch.getState(),"\nStart time:", watch.getStartTime(),\
          "\nEnd time:", watch.getEndTime(), end = "\n\n")
    

main()
