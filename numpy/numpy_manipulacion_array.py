#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 21:30:51 2018

@author: Ruman
"""

import numpy as np

print("**********************************************************************")
print("Cambios de Tamaño:\n")
#array unidimensionales a partir de un rango
a = np.arange(0,1000,10)
print("Original:\n",a,"\n")
aux=a.reshape(4,25)
print("Redimensionado:\n",aux,"\n")

#Cambio de tamaño o de forma. Para ello se puede aplanar la matriz mediante la 
#función ravel() y, a continuación, usar el método shape() o resize() 
#para establecer las nuevas dimensiones

aux2=aux.ravel()
print ("Aplanado:\n",aux2)
aux3=aux2.reshape(10,10)
print ("Redimiensionado:\n",aux3)

print("Dimensiones:",np.ndim(aux3),"\n")
print("Tipo:",aux3.dtype,"\n")
print("Forma:",np.shape(aux3),"\n")


print("**********************************************************************")
print("Fusion:\n")
a = np.arange(0,1000,10).reshape(10,10)
b = np.arange(0,2000,20).reshape(10,10)
print ("Array A:\n",a)
print ("Array B:\n",b)
concat=np.concatenate((a,b),axis=0) #Vertical
print ("Concatenado:\n",concat)
concat=np.concatenate((a,b),axis=1) #Horizontal
print ("Concatenado:\n",concat)


print("**********************************************************************")
print("División:\n")
#Dividir un array en partes iguales usando las funciones hsplit() y vsplit(), 
#indicando la columna o fila por donde se divide dependiendo la función.
a = np.arange(0,1000,10).reshape(10,10)
print("Original:\n",a)
split=np.hsplit(a,2)
print("\nSplit 1:\n",split)
split2=np.vsplit(a,2)
print("\nSplit 2:\n",split2)
#descomponer por filas
b,c,d,e,f,g,h,i,j,k=a
print("\nDescompsoción primera fila:\n",b)
print("\nDescompsoción segunda fila:\n",c)


print("\n**********************************************************************")
print("Asignaciones y Copias:\n")
#Las asignaciones y las llamadas a funciones no hacen copia del array o de sus datos
a = np.arange(0,1000,10).reshape(10,10)
#las dos variables pasan a apuntara a la misma dirección de memoria
b=a
b.shape=(5,20)
print(b)


print("\n**********************************************************************")
print("Vistas:\n")
#Permite crear un nuevo array que toma los datos del array original, 
#pero sin tratarse del mismo. Sin embargo, el array original NOOOO se ve afectado por 
#las operaciones que se hagan sobre la vista. Pero lo único que no se ve afectado son
#los cambios de dimensión. ver https://www.tutorialspoint.com/numpy/numpy_copies_and_views.htm
a=np.array([[2,3,4,2,5],[3,6,5,2,7]]) 
print ("Original:\n",a)
c=a.view()
print ("Vista:\n",c)
c.shape=(5,2)
print ("Original:\n",a)
print ("Vista:\n",c)
c[1,1]=99
print ("Original:\n",a)
print ("Vista:\n",c)


print("\n**********************************************************************")
print("Copia Independiente:\n")
#Permite crear un nuevo array que toma los datos del array original, 
#pero sin tratarse del mismo. Sin embargo, el array original NOOOO se ve afectado por 
#las operaciones que se hagan sobre la vista
a=np.array([[2,3,4,2,5],[3,6,5,2,7]]) 
print ("Original:\n",a)
c=a.copy()
print ("Copia:\n",c)
c[1,1]=99
print ("Original:\n",a)
print ("Copia:\n",c)

print("\n**********************************************************************")
print("Ordenar Arrays:\n")
#Permite crear un nuevo array que toma los datos del array original, 
#pero sin tratarse del mismo. Sin embargo, el array original NOOOO se ve afectado por 
#las operaciones que se hagan sobre la vista
a=np.array([2,3,4,2,5,3,6,5,2,7]) 
print ("Original:\n",a)
a.sort()
print ("Ordenado:\n",a)

b=np.array([[2,3,4,2,5],[3,6,5,2,7]])  
print ("Original:\n",b)
b.sort(0)#columnas
print ("Ordenado Columnas:\n",b)

c=np.array([[2,3,4,2,5],[3,6,5,2,7]])  
print ("Original:\n",c)
c.sort(1)#Filas
print ("Ordenado Filas:\n",c)

print("\n**********************************************************************")
print("Arrays Booleanes:\n")
a=np.array([True, True, False, True, True, False]) 
b=np.array([True, True, True, True, True, True]) 
print("Hay algun valor cierto?:",a.any())
print("Son todos los valores ciertos?:",a.all())

