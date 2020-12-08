# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 09:31:29 2020
@author: jmlop
"""


import pandas as pd
import openpyxl as xl
import xlsxwriter
import os.path
import datetime


def menu():
    veces = 0
    entrada = {'nombre':[],'fecha':[],'animo':[]}
    while True:
        print("          Diario          \n__________________________")
        print("[1] Crear entrada\n[2] Ver entradas previas\n[3] Ver promedio de ánimo\n[0] terminar")
        try:
            p = int(input("Qué desea hacer?\n"))
        except:
            print("Entrada invalida.")
        if p >= 0 and p < 4 and (type(p) is int):
            if p == 1:
                crearE(veces, entrada)
                veces += 1
            elif p == 2:
                verE(entrada)
            elif p == 3:
                print(prom(entrada))
            elif p == 0:
                break
            else:
                print("Ingrese una opción válida")


        



def crearE(x:int, entrada : {}):
    entrada['nombre'].append(input("Ingrese su nombre completo:\n"))
    entrada['fecha'].append(datetime.datetime.now())
    entrada['animo'].append(int(input("Del 1 al 10 ¿Cómo se siente hoy?\n")))



def verE(entrada : {}):
    n, f, a, s = entrada['nombre'], entrada['fecha'], entrada['animo'], ""
    for i in range(len(n)):
        s = "Nombre: " + n[i] + " Fecha: "+ str(f[i]) + " Nivel de ánimo: " + str(a[i])
        print(s)
        
    
def prom(entrada) :
    ac = 0
    if len(entrada['animo']) > 0:
        for i in entrada['animo']:
            ac += i
        ac = ac / len(entrada['animo'])
        return "El promedio de sus entradas de ánimo es " + str(ac)
    else:
        return("No hay registros")

menu()
