# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 19:53:31 2025

@author: Carlos Gil
"""

import math

print('\n\nConverir 1024 a código binario\n\n')

decimal=1024
binario = ''

if decimal == 0:
    binario = '0'

else:
    while decimal > 0:
        residual = decimal % 2
        binario = str(residual) + binario
        decimal = decimal // 2

print('El numero binario de 1024 es', binario)
