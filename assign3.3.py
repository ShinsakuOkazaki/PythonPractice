#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:12:41 2018

@author: sinsakuokazaki
"""
#import math
import math

#latitude and longitude for each city, and convert the number to radians
atlanta = (math.radians(-86.0189), math.radians(40.17428))

florida = (math.radians(-81.52504), math.radians(28.41153))

savannah = (math.radians(-81.19989), math.radians(32.16723))

charlotte = (math.radians(-80.95676), math.radians(35.20724))

#define function to calculate distance between two cities
def distance(x1, y1, x2, y2):
    radius = 6371.01
    result = radius * math.acos(math.sin(x1) * math.sin(x2) * \
                                     math.cos(x1) * math.cos(x2) * \
                                             math.cos(y1 - y2))
    return result

#calculate distance between two cities
dAtlantaFlorida = distance(atlanta[0], atlanta[1], florida[0], florida[1])

dAtlantaSavannah= distance(atlanta[0], atlanta[1], savannah[0], savannah[1])

dAtlantaCharlotte = distance(atlanta[0], atlanta[1], charlotte[0], charlotte[1])

dFloridaSavannah = distance(florida[0], florida[1], savannah[0], savannah[1])

dSavannahCharllote = distance(savannah[0], savannah[1], charlotte[0], charlotte[1])

#define function to calculate area of triagle when polygon is devided into two triangles
def areaOfTriangle(distance1, distance2, distance3):
    s = (distance1 + distance2 + distance3) / 2
    
    result = math.sqrt(s * (s - distance1) * (s - distance2) * (s - distance3))
    
    return result

#calculate areas of two triangles
areaOfTriangle1 = areaOfTriangle(dAtlantaFlorida, dAtlantaSavannah, dFloridaSavannah)
areaOfTriangle2 = areaOfTriangle(dAtlantaCharlotte, dAtlantaSavannah, dSavannahCharllote)

#calculate area of polygon enclosed by four cities
areaOfPolygon = areaOfTriangle1 + areaOfTriangle2

#print the result
print("The area enclosed by the four city is", round(areaOfPolygon, 2))
