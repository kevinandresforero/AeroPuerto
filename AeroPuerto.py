#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   Este es el Servidor
import socket
import pymysql.cursors

#   Usando PyMySQL 

contraseña = "261120"
Db = "Prueba"
Port = 50000
Host = 'localhost'

conexion = pymysql.connect(host="localhost",
                           user="root",
                           passwd=contraseña)

cursor = conexion.cursor()

try:
    cursor.execute("CREATE DATABASE Prueba;")
    print("\nCreando...")
    print("\nSe creo satisfactoriamente la DB Prueba")
    conexion.commit()
except:
    print("\nYa Fue Creada En Otra Ocación la DB Prueba")
cursor.close()
conexion.close()

conexion = pymysql.connect(host="localhost",
                           user="root",
                           passwd=contraseña,
                           database=Db)
try:
    CrearTabla = "CREATE TABLE VuelosClientes (Id int NOT NULL AUTO_INCREMENT,\
    Nombre varchar(50), Cedula int(10) NOT NULL,Origen varchar(30),\
    Destino varchar(30),Hora varchar(5),Fecha DATE,Aerolinea varchar(15),\
    Precio float(8),PRIMARY KEY (Id));"
    cursor = conexion.cursor()
    cursor.execute(CrearTabla)
    conexion.commit()
    
except:
    print("Ya esta Creada La Tabla VuelosClientes")

#   Socket
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Host,Port))

s.listen(1)

conn, addr = s.accept()

while 1:
    datos = conn.recv(1024)
    desencrip = datos.decode("utf-8")
    
    #   Separar Por comas
    datosS = desencrip.split(", ")
    print(datosS)
    
    #   llenar tabla sql
    
    nom = datosS[0]
    ced = datosS[1]
    ori = datosS[2]
    des = datosS[3]
    hor = datosS[4]
    fec = datosS[5]
    aer = datosS[6]
    cos = datosS[7]
    

    sqlIn = "insert into VuelosClientes(\
        Nombre,Cedula,Origen,Destino,Hora,Fecha,Aerolinea,Precio) \
        values(%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sqlIn, (nom, ced, ori, des, hor, fec, aer, cos))
    conexion.commit()
    cursor.close()
    conexion.close()

    if not datos:
        break
    
    try:
        mensajeS = ""
        mensajeSal = "Se pudo Guardar los datos en la DB"
        for i in range(len(datosS)):
            mensajeS += datosS[i]
        conn.sendall(mensajeSal.encode())
    except:
        mensajeS = "Error en la capa 8"
        conn.sendall(mensajeS.encode())

#   Cierro el servidor
conn.close()
s.close()

#   Cierro la conexion interna de la DB
conexion.close()
cursor.close()

"""
Created on Wed Mar  4 08:12:31 2020
@author: Kevin
"""