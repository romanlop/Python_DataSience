#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 22:39:25 2018

@author: Ruman

Un dataframe es una estructura que contiene una colección ordenada de columnas, 
cada una de las cuales puede tener valores de diferentes tipos. Está formado 
por datos, opcionalmente un índice (etiquetas de las filas) y un conjunto de 
columnas (etiquetas de las columnas). En caso de no existir un índice, se genera 
a partir de los datos.

"""

import pandas as pd
import csv 
import numpy as np


#devuelve el contenido del fichero csv
def lectura_csv(file_toOpen):
    with open(file_toOpen) as file_csv: 
        lector=csv.reader(file_csv,delimiter=';')
        lista=list(lector)
        contenido=np.array(lista)
    return contenido


#Programa Principal
    
#Recuperamos las colunas que nos interesa y las pasamos a int para poder realizar calculos
contenido=lectura_csv("csv/est_pasajeros.csv")
fechas=contenido[1:,0]
p_nacion=contenido[1:,4]
p_nacion=p_nacion.astype(int)
p_inter=contenido[1:,5]
p_inter=p_inter.astype(int)
p_totales=p_nacion+p_inter

print("***************************")
#podemos crear un dataframe de un diccionario de ndarray
df=pd.DataFrame({'fechas':fechas,'nacionales':p_nacion,'Internacionales':p_inter,'Totales':p_totales})
print(df)
print("***************************")
#podemos crear un dataframe a partir de una lista de diccionarios
d= [{'a':0, 'b':1, 'c':2},{'f':300, 'g':400, 'h':500}]
print (d)
df=pd.DataFrame(d)
print (df)
print("***************************")
#las claves del diccionario actuan como etiquetas de las columnas
d= [{'a':0, 'b':1, 'c':2},{'a':300, 'b':400, 'c':500}]
print (d)
df=pd.DataFrame(d)
print (df)
print("***************************")
#Se pueden especificar las etiquetas de las filas
df2=pd.DataFrame(d, index=['first','second'])
print (df2)
print("***************************")
#Se puede crear como un diccionario de series
s= {'One': pd.Series([45, 13, 53, 234],index=['a','b','c','d']),'Two': pd.Series([452, 123, 353, 2234],index=['a','b','c','d'])}
print(pd.DataFrame(s))
s2= {'One': pd.Series([45, 13, 53, 234],index=['a','b','c','d']),'Two': pd.Series([452, 123, 353, 2234],index=['a','r','y','d'])}
print(pd.DataFrame(s2))
print(pd.DataFrame(s2,index=['a','b']))
print("***************************")
#Si no se pasan columnas
s= {'One': pd.Series([45, 13, 53, 234]),'Two': pd.Series([452, 123, 353, 2234])}
print(pd.DataFrame(s))

print("***************************")
#Array Estructurado


