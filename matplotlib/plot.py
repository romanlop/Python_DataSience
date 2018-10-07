#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 14:21:15 2018

@author: Ruman
"""

import matplotlib.pyplot as plt
import csv 
import numpy as np
from collections import Counter
from operator import itemgetter



#definición de funciones

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
fechas=contenido[1:12,0]
p_nacion=contenido[1:12,4]
p_nacion=p_nacion.astype(int)
p_inter=contenido[1:12,5]
p_inter=p_inter.astype(int)
p_totales=p_nacion+p_inter
print(fechas)
print(p_totales)

plt.plot(p_nacion,p_inter)
plt.show()
#vuelos nacionales, internacionales y totales
plt.plot(p_nacion, 'r:s',label="Nacionales")
plt.plot(p_inter,label="Internacionales")
plt.plot(p_totales,label="Totales")
#opciones
plt.xticks(range(12),fechas)
plt.xlabel('Fechas')
plt.ylabel('Pasajeros')
plt.title('Pasajeros México')
plt.grid(True)
plt.legend()
#texto situado en base al eje de coordenadas. A sus valores
plt.text(7,41000,'Mi primer gráfico!!!')
#texto situado en base al gráfico
plt.figtext(0.7,0.5,'Caralludo!!!')
plt.annotate("Máximo",xy=(2.2,55000),xytext=(3,54000),arrowprops=dict(facecolor="green",shrink=0.01,headlength=3))
plt.show()


#Histogramas:Los histogramas son un tipo de gráficos que permiten visualizar 
#las frecuencias de aparición de un conjunto de datos en forma de barras. 
#La superficie de cada barra define una categoría que es proporcional a la 
#frecuencia de los valores representados
estados=contenido[1:30,2]
plt.figure(figsize=(20,5))
plt.hist(estados,25)



#ordenarlo por estados
