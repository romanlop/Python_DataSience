#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 12:59:56 2018

@author: Ruman
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

    
#Recuperamos las colunas que nos interesa y las pasamos a int para poder realizar calculos
#contenido es un nparray
contenido=lectura_csv("csv/est_pasajeros.csv")
fechas=contenido[1:40,0]
p_nacion=contenido[1:40,4]
p_nacion=p_nacion.astype(int)
p_inter=contenido[1:40,5]
p_inter=p_inter.astype(int)


#Creamos el DataFrame
s= {'Fechas': pd.Series(fechas),'Nacionales': pd.Series(p_nacion), 'Internacionales':pd.Series(p_inter)}
ds=pd.DataFrame(s)
print("DataFrame vuelos:\n",ds)
#Un dataframe es como un diccionario de series indexado, por lo que se pueden 
#usar las mismas operaciones utilizadas con los diccionarios
print("***************************")
print("Fechas:\n",ds['Fechas'])
print("\nNacionales:\n",ds['Nacionales'])

print("***************************")
ds['Totales']=ds['Nacionales']+ds['Internacionales']
print("DataFrame vuelos con totales:\n",ds)

print("***************************")
mascara=ds['Totales']>15000
print("Fechas con mas de 20000 vuelos:\n",ds[mascara])


#ACCESO POR FILAS / ETIQUETAS
print("***************************")
print(ds.index)
print("Acceso a una fila concreta:\n",ds.loc[25])

#BORRAR COLUMNAS
print("***************************")
del(ds['Totales'])
print("Eliminación de elementos:\n",ds)
#Devuelve el elemento y lo borra
internacionales=ds.pop('Internacionales')
print(internacionales)
    
#Insertar columnas
print("***************************")
ds['Internacionales']=p_inter
#Vamos a incluir totales pero como segunda columna
ds.insert(1,'Totales',ds['Nacionales']+ds['Internacionales'])
print("Inserción de elementos:\n",ds)


#Selección por rangos
print("***************************")
print("Inserción de elementos:\n",ds.loc[5:10])


#Operaciones sobre columnas
print("***************************")
ds['Totales']=ds['Totales']*5
print("DataFrame vuelos:\n",ds)

#Transponer el array
print("***************************")
print("Transposición:",ds[:20].T)

print("Transposición:",ds[1:2].T)

#Pintar el array
print("***************************")
print("Info:",ds.info())
print("Info:",ds.to_string())
