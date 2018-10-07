#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 14:55:07 2018

@author: Ruman

1)Crea un nuevo archivo CSV denominado AcumAnnos.csv que contenga la frecuencia de los años. Tendrá la estructura:
Años,Frecuencia
1980,2
1981,6
"""

import csv 
from collections import Counter
from operator import itemgetter

#definición de funciones

#devuelve el contenido del fichero csv
def lectura_csv(file_toOpen):
    file_csv=open(file_toOpen) 
    lector=csv.reader(file_csv)
    content=list(lector)
    return content

#crea un csv con la frecuencia del campo "year"
def frecuencia_year(list_content,file_dest,column,list_header):
    lista=[]
    print (list_header)
    for linea in list_content:
        lista.append(linea[column])
    frecuency = Counter(lista[1:]) 
    with open(file_dest, 'x') as f:  
        escritor=csv.writer(f)
        escritor.writerow(list_header)
        for x, y in frecuency.items():
            escritor.writerow([x,y])
    return 1


#crea un csv con la frecuencia del campo "year"
def sort_byname(list_content,file_dest):
    lista_ordenada=sorted(list_content, key=itemgetter(0))
    with open(file_dest, 'x') as f:  
        escritor=csv.writer(f)
        for x in lista_ordenada:
            escritor.writerow(x)
    return 1


    
#Programa Principal
contenido=lectura_csv("PitchingPost.csv")
l=["año","frecuencia"]
frecuencia_year(contenido,"frecuencia_year.csv",1,l)
l=["jugador","frecuencia"]
frecuencia_year(contenido,"frecuencia_player.csv",0,l)
sort_byname(contenido,"sorted.csv")

