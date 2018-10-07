#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 10:20:50 2018

@author: Ruman

El módulo NumPy (Numerical Python) es una extensión de Python que proporciona 
funciones y rutinas matemáticas para la manipulación de arrays y matrices de 
datos numéricos de una forma eficiente.

El elemento esencial de NumPy son unos objetos denominados ndarray, 
arrays multidimensionales donde todos sus elementos son del mismo tipo y están 
indexados por una tupla de números positivos.

Su principal ventaja es la eficiencia para manipular vectores y matrices. 
En este sentido, proporciona funciones que operan sobre ndarrays.
"""

import numpy as np

#crea un ndarray con valores aleatorios
array_prueba=np.random.random((3,3,3,3))

print(array_prueba,"\n")
print("Dimensiones:",np.ndim(array_prueba),"\n")
print("Tipo:",array_prueba.dtype,"\n")
print("Forma:",np.shape(array_prueba),"\n")
print("Número de elementos:",np.size(array_prueba),"\n")
print("Tamaño en bytes de cada elemento:",array_prueba.itemsize,"\n")

print("**************************************************\n")
#crear arrays con array()
a = np.array([[2,3,4],[3,6,5]])
print(a,"\n")
print("Dimensiones:",np.ndim(a),"\n")
print("Tipo:",a.dtype,"\n")
print("Forma:",np.shape(a),"\n")
print("Número de elementos:",np.size(a),"\n")
print("Tamaño en bytes de cada elemento:",a.itemsize,"\n")

print("**************************************************\n")
#array unidimensionales a partir de un rango
a = np.arange(0,1000,10)
print(a,"\n")
print("Dimensiones:",np.ndim(a),"\n")
print("Tipo:",a.dtype,"\n")
print("Forma:",np.shape(a),"\n")
print("Número de elementos:",np.size(a),"\n")
print("Tamaño en bytes de cada elemento:",a.itemsize,"\n")

print("**************************************************\n")
#Se puede redimensionar el array que genera arange() 
#mediante el método reshape()
b = a.reshape(10,10)
print(b,"\n")
print("Dimensiones:",np.ndim(b),"\n")
print("Tipo:",b.dtype,"\n")
print("Forma:",np.shape(b),"\n")
print("Número de elementos:",np.size(b),"\n")
print("Tamaño en bytes de cada elemento:",b.itemsize,"\n")

print("**************************************************\n")
#linspace (figura 6.6.), que también genera una secuencia de números a partir 
#de un rango dado para crear un array, pero recibe como tercer argumento el 
#número de elementos, en vez de la distancia entre ellos.
a = np.linspace(0,10,25)
print(a,"\n")
print("Dimensiones:",np.ndim(a),"\n")
print("Tipo:",a.dtype,"\n")
print("Forma:",np.shape(a),"\n")
print("Número de elementos:",np.size(a),"\n")
print("Tamaño en bytes de cada elemento:",a.itemsize,"\n")

print("**************************************************\n")
#Creación de un array unidimensional con datos aleatorios mediante la función 
#rand del módulo Random (figura 6.7.). La función rand devuelve un número 
#aleatorio procedente de una distribución uniforme en el intervalo [0,1].
a = np.random.rand(100)
print(a,"\n")
print("Dimensiones:",np.ndim(a),"\n")
print("Tipo:",a.dtype,"\n")
print("Forma:",np.shape(a),"\n")
print("Número de elementos:",np.size(a),"\n")
print("Tamaño en bytes de cada elemento:",a.itemsize,"\n")

print("**************************************************\n")
#Existen funciones que generan arrays especiales que solo requieren como 
#argumento el tamaño del array (figura 6.9.)
#ceros
a = np.zeros((10,10),dtype=np.int8)
print(a,"\n")
print("Dimensiones:",np.ndim(a),"\n")
print("Tipo:",a.dtype,"\n")
print("Forma:",np.shape(a),"\n")
print("Número de elementos:",np.size(a),"\n")
print("Tamaño en bytes de cada elemento:",a.itemsize,"\n")
#unos
a = np.ones((10,10),dtype=np.int8)
print(a,"\n")
print("Dimensiones:",np.ndim(a),"\n")
print("Tipo:",a.dtype,"\n")
print("Forma:",np.shape(a),"\n")
print("Número de elementos:",np.size(a),"\n")
print("Tamaño en bytes de cada elemento:",a.itemsize,"\n")
#aleatorio
a = np.empty((10,10))
print(a,"\n")
print("Dimensiones:",np.ndim(a),"\n")
print("Tipo:",a.dtype,"\n")
print("Forma:",np.shape(a),"\n")
print("Número de elementos:",np.size(a),"\n")
print("Tamaño en bytes de cada elemento:",a.itemsize,"\n")






















