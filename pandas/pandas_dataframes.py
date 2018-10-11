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


#podemos crear un dataframe de un diccionario de ndarray
df=pd.DataFrame({'fechas':fechas,'nacionales':p_nacion,'Internacionales':p_inter,'Totales':p_totales})
print(df)
