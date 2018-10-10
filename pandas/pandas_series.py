#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 22:09:56 2018

@author: Ruman
"""

import pandas as pd

#Objeto "Serie" es un objeto, como un array, que está formado por un array de 
#datos y un array de etiquetas denominado índice.

#ndarray: longitud de los índices = que el nñumero de datos.
print("**********NDARRAY**********")
s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s)
#sin indice
s1 = pd.Series([1,2,3,4,5])
print(s1)

#Diccionario . Si se le pasa un diccionario se asocian los valores a los elementos del índice
print("**********DICCIONARIO**********")
d= {'a':0, 'b':1, 'c':2}
s2= pd.Series(d,index=['b','c','d','a','a'])
print (s2)
#sin indice, mantiene las claves ordenadas del diccionario original
s3= pd.Series(d)
print (s3)

#Valor Escalar
print("**********ESCALAR**********")
s4= pd.Series(100,index=['b','c','d','a','a'])
print (s4)
print("***************************")
#Las series actúan de forma similar a ndarray, siendo un argumento
#válido de funciones de NumPy (figura 6.68.).
s4= pd.Series([1,2,3,4,5],index=['b','c','d','a','a'])
s5=s4[s4 > s4.median()]
print(s5)
print(s4[[4,3,1]])

print("***************************")
#Las series actúan como un diccionario de tamaño fijo en el que se pueden 
#gestionar los valores a través de los índices
s4= pd.Series([1,2,3,4,5],index=['b','c','d','a','a'])
print(s4['a'])
s4['a']=[66,55.4] #como inicialmente son enteros parace que "castea" el 55.4
print(s4['a'])
print('b' in s4)

print("***************************")
#Permiten Operaciones Vectoriales
s6=s4+s
print (s6)

#La principal diferencia entre series y ndarray es que las operaciones 
#entre series alinean automáticamente los datos basados en las etiquetas