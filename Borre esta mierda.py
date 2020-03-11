#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql.cursors
import tkinter as tk

contraseña = "261120"
Db = "Prueba"

conexion = pymysql.connect(host="localhost",
                           user="root",
                           passwd=contraseña,
                           database=Db)

#   Consulta por CedulA
def Consulc():
    criterio = tk.Entry(marco,width = 20, bg="red" , fg="black")
    criterio.grid(row=5,column=1,sticky=tk.W,pady=4)
    
    tk.Label(marco, text="Consultar tabla por Cédula", bg="black", fg="red").grid(row=5,
                                                                                   column=0)
    
    def EjecutarConsulta():
        
        Cedula = int(criterio.get())
        bc = "SELECT Nombre,Cedula,Origen,Destino,Hora,Fecha,Aerolinea,Precio\
         FROM VuelosClientes WHERE Cedula = %s"
         
        cursor = conexion.cursor()
        cursor.execute(bc,(Cedula,))
        #       Separar Consulta  9 Campos
        aux=0
        for i in cursor:
            print(i[aux])
            aux = aux + 1
        
    tk.Button(marco, text="Consultar", command=EjecutarConsulta, bg="black", fg="red").grid(row=5,
                                                                   column=2,
                                                                   sticky=tk.W,
                                                                   pady=4,padx=4)
# Consulta por Destino
def ConsulD():
    criterio = tk.Entry(marco,width = 20, bg="red" , fg="black")
    criterio.grid(row=7,column=1,sticky=tk.W,pady=4)
    
    tk.Label(marco, text="Consultar tabla por Destino", bg="black", fg="red").grid(row=7,
                                                                                   column=0)
    
    def EjecutarConsulta():
        
        Destino = str(criterio.get())
        bc = "SELECT Nombre,Cedula,Origen,Destino,Hora,Fecha,Aerolinea,Precio\
         FROM VuelosClientes WHERE Destino = %s"
         
        cursor = conexion.cursor()
        cursor.execute(bc,(Destino,))
        #       Separar Consulta  9 Campos
        aux=0
        for i in cursor:
            print(i[aux])
            aux = aux + 1
        
    tk.Button(marco, text="Consultar", command=EjecutarConsulta, bg="black", fg="red").grid(row=7,
                                                                   column=2,
                                                                   sticky=tk.W,
                                                                   pady=4,
                                                                   padx=4)
# Consulta por Aerolinea

def ConsulA():
    criterio = tk.Entry(marco,width = 20, bg="red" , fg="black")
    criterio.grid(row=9,column=1,sticky=tk.W,pady=4)
    
    tk.Label(marco, text="Consultar tabla por Aerolinea", bg="black", fg="red").grid(row=9,
                                                                                   column=0)
    
    def EjecutarConsulta():
        
        Aerolinea = str(criterio.get())
        bc = "SELECT Nombre,Cedula,Origen,Destino,Hora,Fecha,Aerolinea,Precio\
         FROM VuelosClientes WHERE Aerolinea = %s"
         
        cursor = conexion.cursor()
        cursor.execute(bc,(Aerolinea,))
        #       Separar Consulta  9 Campos
        aux=0
        for i in cursor:
            print(i[aux])
            aux = aux + 1
        
    tk.Button(marco, text="Consultar", command=EjecutarConsulta, bg="black", fg="red").grid(row=9,
                                                                   column=2,
                                                                   sticky=tk.W,
                                                                   pady=4,padx=4)
# Consulta por fecha
def ConsulF():
    criterio = tk.Entry(marco,width = 20, bg="red" , fg="black")
    criterio.grid(row=11,column=1,sticky=tk.W,pady=4)
    
    tk.Label(marco, text="Consultar tabla por Fecha", bg="black", fg="red").grid(row=11,
                                                                                   column=0)
    
    def EjecutarConsulta():
        
        Aerolinea = str(criterio.get())
        bc = "SELECT Nombre,Cedula,Origen,Destino,Hora,Fecha,Aerolinea,Precio\
         FROM VuelosClientes WHERE Fecha = %s"
         
        cursor = conexion.cursor()
        cursor.execute(bc,(Aerolinea,))
        #       Separar Consulta  9 Campos
        aux=0
        for i in cursor:
            print(i[aux])
            aux = aux + 1
        
    tk.Button(marco, text="Consultar", command=EjecutarConsulta, bg="black", fg="red").grid(row=11,
                                                                   column=2,
                                                                   sticky=tk.W,
                                                                   pady=4,padx=4)

marco = tk.Tk()
marco.title("Consultar Clientes")
marco.geometry("700x700")
marco.configure(bg="black")
    
def cerrar():
    marco.destroy()


l1 = tk.Label(marco, text="Consultar tabla por origen", bg="black", fg="red")
l1.grid(row=0,column=0)
l2 = tk.Label(marco, text="Consultar tabla por destino", bg="black", fg="red")
l2.grid(row=1,column=0)
l3 = tk.Label(marco, text="Consultar tabla por aerolinea", bg="black", fg="red")
l3.grid(row=2,column=0)
l4 = tk.Label(marco, text="Consultar tabla por fecha", bg="black", fg="red")
l4.grid(row=3,column=0)

tk.Button(marco, text="Consultar", command=Consulc, bg="black", fg="red").grid(row=0,
                                                                       column=1,
                                                                       sticky=tk.W,
                                                                       pady=4)

tk.Button(marco,text="Consultar", command=ConsulD, bg="black", fg="red").grid(row=1,
                                                                       column=1,
                                                                       sticky=tk.W,
                                                                       pady=4)

tk.Button(marco,text="Consultar", command=ConsulA, bg="black", fg="red").grid(row=2,
                                                                       column=1,
                                                                       sticky=tk.W,
                                                                       pady=4)

tk.Button(marco,text="Consultar", command=ConsulF, bg="black", fg="red").grid(row=3,
                                                                       column=1,
                                                                       sticky=tk.W,
                                                                       pady=4)

tk.Button(marco,text="Cerrar", command=cerrar, bg="black", fg="red").grid(row=0,
                                                                    column=10,
                                                                    sticky=tk.W,
                                                                    pady=4,
                                                                    padx=45)


marco.mainloop()

"""
Created on Mon Mar  9 09:27:31 2020
@author: Kevin
"""

