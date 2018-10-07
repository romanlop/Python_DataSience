#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:32:11 2018

@author: Ruman

En NumPy se puede operar aritméticamente sobre los arrays como si se tratara 
de escalares
"""
import numpy as np

a=np.random.random((4,4))
print ("A=\n",a)

b=np.array([[2,3,4,2],[3,6,5,2],[1,1,1,1],[4,4,4,4]])
print ("B=\n",b)
print("**************************************************\n")
print("\nOperaciones básicas:")

print ("\n1.Suma de a y b =\n", a + b)


print ("\n2.Resta de a y b =\n", a - b)

c=a*b
print ("\n3-Multiplicación de a y b =\n", c)


print("\nCuando se opera con arrays de diferente tipo, el tipo del array resultante corresponde al más general.")
print (a.dtype)
print (b.dtype)
print (c.dtype)

print("**************************************************\n")
print("Funciones Universales:")
#Estas funciones operan elemento a elemento y generan como resultado un nuevo array
print ("B^2:\n",np.square(b))
print ("Raiz Cuadrada\n",np.sqrt(b))
#El producto de matrices es posible si el número de columnas de la primera fila es igual al numero de filas del segundo.
a=np.array([[2,3,4,2],[3,6,5,2]]) #matriz 2x4
b=np.array([[2,3,4,2],[3,6,5,2],[1,1,1,1],[4,4,4,4]]) #matriz 4x4
print ("Multiplicación Matricial\n",np.dot(a,b))

"""
Existen algunas operaciones implementadas como métodos de la clase ndarray y, 
por defecto, se aplican a todos los elementos del array. Sin embargo, es 
posible especificar la dimensión sobre la que se quiere aplicar la operación 
mediante el argumento axis (figura 6.14.) que toma el valor 0 (columnas) o 1 (filas).
"""
print ("\nA=",a)
print ("\nUso de Axis. La suma de elementos de a es:",a.sum())
print ("\nSi usamos Axis, la suma de elementos de a es:",a.sum(axis=0))


print("**************************************************\n")
print("Operadores a+= y a*=:")

a+=100
print ("Matriz a + 100\n", a)









