#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:20:19 2018

@author: Ruman

Crear una serie denominada "Sueldos_hombres" que contenga los datos [2500,1800,1900,2000,2100] 
y cuyos índices sean ["Euskadi", "Murcia", "Madrid", "Barcelona", "Zaragoza"], 
y otro denominada "Sueldos_mujeres" que contenga los datos [2300,1600,1980,1900,2150] 
y cuyos índices sean ["Euskadi", "Murcia", "Madrid", "Barcelona","Córdoba"]

Usando las series anteriores, obtén otra serie que contenga la diferencia de 
sueldos entre mujeres y hombres.

Usando la serie anterior que contiene las diferencias de sueldos, obtén las c
iudades donde la diferencia de sueldos es mayor de 100 €.
"""

import pandas as pd

print("PRACTICA FINAL**************************************")
sueldos_h = pd.Series([2500,1800,1900,2000,2100],index=['Euskadi','Murcia','Madrid','Barcelona','Zaragoza'])
sueldos_m = pd.Series([2300,1600,1980,1900,2150],index=['Euskadi','Murcia','Madrid','Barcelona','Córdoba'])
print("OPCION 1**************************************")
#Opción 1:
sueldos_dif=sueldos_h-sueldos_m
print("Diferencia Sueldos:",sueldos_dif)
print("OPCION 2**************************************")
#Opción 2 con DataFrames
sueldos_df=pd.DataFrame([sueldos_h,sueldos_m])
#Transponemos
sueldos_df=sueldos_df[:].T
#Calcular la difernecia
sueldos_df['2']=sueldos_df[0]-sueldos_df[1]
#Ponemos etoquetas a las columnas
sueldos_df.columns=['Sueldo Hombres','Sueldo Mujeres','Diferencia']
print(sueldos_df)

print("Diferencia mayor que 100****************")
mascara=abs(sueldos_df['Diferencia'])>50
print("Fechas con mas de 20000 vuelos:\n",sueldos_df[mascara])