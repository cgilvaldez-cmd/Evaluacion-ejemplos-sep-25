# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 16:17:07 2025

@author: Carlos Gil
"""

import math

x= [1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00, 11.00, 12.00]
y= [1.23, 2.13, 1.42, -0.69, 4.29, 3.64, 9.30, 10.62, 7.42, 8.40, 12.30, 10.30]

sum_x = sum(x)
media_y= sum(y)/12 
media_x= sum(x)/12

sum_xy= 0
long= len(y) 
for i in range(long):
    sum_xy += (y[i]**2 )
print ('La suma de la multiplicacion de xy es', sum_xy)

def sum_cuad_for(x):
    suma=0
    for x in x:
        suma += x**2
    return suma
print('La sumatoria de cuadrados de x es', sum_cuad_for(x))

sq = (sum_x)**2
sqnum= sq/12
print('La sumatoria de x al cuadrado es', sqnum)


t1= (sum_xy-(12*(media_y*media_x)))
t2 = ((sum_cuad_for(x))-sqnum)  

total=(t1/t2)

print('La pendiente es', total)

Intercepto= (media_y-(total*(media_x)))
print('El intercepto es', Intercepto)

