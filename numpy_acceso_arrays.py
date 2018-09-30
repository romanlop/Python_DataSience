#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 20:11:36 2018

@author: Ruman
"""

import numpy as np
#array unidimensionales a partir de un rango
a = np.arange(0,1000,10)
print(a,"\n")
print("Dimensiones:",np.ndim(a),"\n")
print("Tipo:",a.dtype,"\n")
print("Forma:",np.shape(a),"\n")
print("Número de elementos:",np.size(a),"\n")
print("Tamaño en bytes de cada elemento:",a.itemsize,"\n")

#Cuando trabajamos con arrays de una dimensión, el acceso a los elementos se 
#realiza de forma similar al de las listas o tuplas de elementos 

print("El elemento 50 es:",a[50])
print("Los elementos 0 a 30 son:",a[0:30])
print("Los elementos 0 a 30 pero de dos en dos:",a[0:30:2])
#no es necesario indicar el final del array
print("Los elementos de 0 a 100 de 30 en 30:",a[0::30])

#Una diferencia importante con las listas es que las particiones de un ndarray 
#mediante la notación [inicio:fin:paso] son vistas del array original. Todos los
#cambios realizados en las vistas se reflejan en el array original 
print ("\nDiferencia con listas:")
b=a[25:50:1]
b[::]=1
print (a)

print("\n**************************************************")
print ("\nAcceso a Arrays Multidimensionales:")
array_prueba=np.random.random((4,4,4))
print(array_prueba,"\n")
print ("\nAcceso a elemento concreto:\n",array_prueba[1,0,2])
print ("Acceso a fila 3 de cada dimension:\n",array_prueba[0:4,2])
print ("Acceso a fila 3 columna 3 de cada una de las 4 dimensiones:\n",array_prueba[0:4,2,2])

print("\n**************************************************")
print ("\nAcceso mediante mascaras:")
mascara = array_prueba < 0.5
print ("Array con valores < 0.5:",array_prueba[mascara])

#Para iterar sobre multimensionales es mejor utilizar "flat"
for i in array_prueba:
    print (i,"\n")
    
for i in array_prueba.flat:
    print (i,"\n")