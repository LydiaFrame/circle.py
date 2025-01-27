#!/usr/bin/env python3

"""Write a program to calculate the area and circumference of a circle"""

__author__="Lydia Frame"
__date__="01/26/2025"

PI = 3.14

#Prompt user for radius 
radius = float(input("Radius: "))
print()

#Calculate area and circumference 
area = round(PI*radius**2, 3)
circumference = round(2*PI*radius, 3)

#outpute area and circumference 
print("Area: " + str(area))
print("Circumference: " + str(circumference))