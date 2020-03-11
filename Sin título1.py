#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql.cursors

contraseña = "261120"
Db = "Prueba"

conexion = pymysql.connect(host="localhost",
                           user="root",
                           passwd=contraseña,
                           database=Db)

cursor = conexion.cursor()

try:
    Relaciones = """CREATE TABLE Relaciones(
                    idE_foran int NOT NULL,
                    idM_foran int NOT NULL,
                    FOREIGN KEY (idE_foran) REFERENCES Students(IdE),
                    FOREIGN KEY (idM_foran) REFERENCES Materias(idM)
                    );"""
    cursor.execute(Relaciones)
    print("\nCreando tabla Relaciones...")
    print("\nTabla Relaciones creada satisfactoriamente")
    conexion.commit()
except:
    print("\nYa está creada la tabla Relaciones")

#try:
#            MostrarTablaEs = "select * from  Students"
#            cursor.execute(MostrarTablaEs)
#            record = cursor.fetchall()
#            for fila in record:
#                print("{:<4} {:<4}".format(fila[0], fila[1]))
#            print("\n")

"""
Created on Thu Mar  5 13:22:40 2020
@author: Kevin
"""

