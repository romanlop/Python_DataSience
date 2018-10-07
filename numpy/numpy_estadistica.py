#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:13:52 2018

@author: Ruman
"""

import numpy as np

a = np.array([[2,3,4,5,77,55,33,88,99,343,44,55,22,11,33,44,55,66,88],[2,3,4,5,24,55,22,88,11,233,44,55,54,11,33,44,523,66,12]])
print(a,"\n")
print("********************************************")
#suma
print ("Suma total:",np.sum(a))
print ("Suma por columnas:",np.sum(a,axis=0))
print ("Suma por filas:",np.sum(a,axis=1))

print("********************************************")
#Maximos y mínimos
print ("Maximo:",np.max(a)," Posicion:",np.argmax(a))
print ("Minimo:",np.min(a)," Posicion:",np.argmin(a))

print("********************************************")
#Media
print ("Media:",np.mean(a))
print ("Media por filas:",np.mean(a,axis=1))

print("********************************************")
#Media y mediana
print ("Media:",np.mean(a))
print ("Media por filas:",np.mean(a,axis=1))
#Representa el valor de la variable de posición central en un conjunto de datos ordenados.
print ("Mediana:",np.median(a))
print ("Mediana por filas:",np.median(a,axis=1))

print("********************************************")
#Varianza: es una medida de dispersion. Es el sumario de (x[i]-media])^2/numero de elementos.
#https://www.youtube.com/watch?v=mZlXDAUQoPU
print ("Varianza:",np.var(a))
#La desviación estándar es una medida de dispersión de una variable que se 
#define como la raíz cuadrada de la varianza de la variable.
print ("Desviación Estandar:",np.sqrt(np.var(a)))
print ("Desviación Estandar:",np.std(a))
print ("Varianza por filas:",np.var(a,axis=1))
print ("Desviación Estandar por filas:",np.sqrt(np.var(a,axis=1)))


print("********************************************")
#Covarianza: Determina si existe una dependencia entre dos variables aleatorias
#https://www.youtube.com/watch?v=1qkAU--IK8Y
#Covarianza positiva representa una relación directa.
#Covarianza negativa representa una relación inversa.
#Si no hay relación el índice de correlación tiende a cero. Tb puede indicar una relación no lineal
x = np.array([[0, 2], [1, 1], [2, 0]]).T
print ("Covarianza:",np.cov(x))
print ("Covarianza:",np.cov(a))

#Indice de Correlación de Person es una correción sobre la Covarianza. En la práctica
#se suele usar esto y no la covarianza. Es la covarianza / prodcuto de las desviaciones típicas de las variables.
#Importate, es un valor adimensional. Tiene siempre una dimension 1.
print ("Indice de correlación de Pearson:",np.corrcoef(x))
print ("Indice de correlación de Pearson:",np.corrcoef(a))


print("********************************************")
#Creación de arrays en base a la distribución normal -> Gauss.
print(np.random.normal(size=(5,2)))


