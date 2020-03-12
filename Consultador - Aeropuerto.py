#!import pymysql.cursors
import tkinter as tk
from tkinter import *
import pymysql

contraseña = "261120"
Db = "Prueba"

conexion = pymysql.connect(host="localhost",
                           user="root",
                           passwd=contraseña,
                           database=Db)


#   Consulta por Cedula


def EjecutarConsultaCedula():

    nueva_ventana = tk.Toplevel(marco)
    nueva_ventana.title("Consulta")
    nueva_ventana.geometry("800x400")
    nueva_ventana.configure(bg="black")

    def cierra_nueva():
        nueva_ventana.destroy()

    tk.Button(nueva_ventana, text="Cerrar", command=cierra_nueva, bg="black", fg="red").grid(row=2,
                                                                                             column=0,
                                                                                             sticky=tk.W,
                                                                                             pady=4)

    Cedula = int(criterioCedula.get())
    bc = "SELECT Nombre,Cedula,Origen,Destino,Hora,Fecha,Aerolinea,Precio\
     FROM VuelosClientes WHERE Cedula = %s"

    cursor = conexion.cursor()
    cursor.execute(bc, (Cedula,))

    datos2 = cursor.fetchall()
    datos = tk.StringVar()
    datos.set(datos2)


    t1 = tk.Text(nueva_ventana)
    t1.grid(row=2,
            column=0,
            sticky=tk.W,
            pady=4)
    for dtos in record:
        t1.insert(END, dtos)
        t1.insert(END, "\n")

    l1 = tk.Label(nueva_ventana, text="Registro con esta información:", bg="black", fg="red").grid(row=0,

                                                                                                   column=0)
#    l2 = tk.Label(nueva_ventana, textvariable=datos).grid(row=1,
#                                                          column=0)


# Consulta por Destino

def EjecutarConsultaDestino():
    nueva_ventana = tk.Toplevel(marco)
    nueva_ventana.title("Consulta")
    nueva_ventana.geometry("800x400")
    nueva_ventana.configure(bg="black")

    def cierra_nueva():
        nueva_ventana.destroy()

    tk.Button(nueva_ventana, text="Cerrar", command=cierra_nueva, bg="black", fg="red").grid(row=2,
                                                                                             column=0,
                                                                                             sticky=tk.W,
                                                                                             pady=4)

    Destino = str(criterioDestino.get())

    bc = "SELECT Nombre,Cedula,Origen,Destino,Hora,Fecha,Aerolinea,Precio\
     FROM VuelosClientes WHERE Destino = %s"

    cursor = conexion.cursor()
    cursor.execute(bc, (Destino,))

    datos2 = list(cursor)
    datos = tk.StringVar()
    datos.set(datos2)


    t1 = tk.Text(nueva_ventana)
    t1.grid(row=2,
            column=0,
            sticky=tk.W,
            pady=4)
    for dtos in record:
        t1.insert(END, dtos)
        t1.insert(END, "\n")

    l1 = tk.Label(nueva_ventana, text="Registro con esta información:", bg="black", fg="red").grid(row=0,
                                                                                                   column=0)
#    l2 = tk.Label(nueva_ventana, textvariable=datos).grid(row=1,
#                                                          column=0)
#

# Consulta por Aerolinea

def EjecutarConsultaAerolinea():
    nueva_ventana = tk.Toplevel(marco)
    nueva_ventana.title("Consulta")
    nueva_ventana.geometry("800x400")
    nueva_ventana.configure(bg="black")

    def cierra_nueva():
        nueva_ventana.destroy()

    tk.Button(nueva_ventana, text="Cerrar", command=cierra_nueva, bg="black", fg="red").grid(row=2,
                                                                                             column=0,
                                                                                             sticky=tk.W,
                                                                                             pady=4)

    Aerolinea = str(criterioAerolinea.get())
    bc = "SELECT Nombre,Cedula,Origen,Destino,Hora,Fecha,Aerolinea,Precio\
     FROM VuelosClientes WHERE Aerolinea = %s"

    cursor = conexion.cursor()
    cursor.execute(bc, (Aerolinea,))

    datos2 = cursor.fetchall()
    datos = tk.StringVar()
    datos.set(datos2)


    t1 = tk.Text(nueva_ventana)
    t1.grid(row=2,
            column=0,
            sticky=tk.W,
            pady=4)
    for dtos in record:
        t1.insert(END, dtos)
        t1.insert(END, "\n")
#
    l1 = tk.Label(nueva_ventana, text="Registro con esta información:", bg="black", fg="red").grid(row=0,
                                                                                                   column=0)
##    l2 = tk.Label(nueva_ventana, textvariable=datos).grid(row=1,
#                                                          column=0)

# Consulta por fecha


def EjecutarConsultaFecha():
    nueva_ventana = tk.Toplevel(marco)
    nueva_ventana.title("Consulta")
    nueva_ventana.geometry("800x400")
    nueva_ventana.configure(bg="black")

    def cierra_nueva():
        nueva_ventana.destroy()

    tk.Button(nueva_ventana, text="Cerrar", command=cierra_nueva, bg="black", fg="red").grid(row=2,
                                                                                             column=0,
                                                                                             sticky=tk.W,
                                                                                             pady=4)

    Fecha = str(criterioFecha.get())
    bc = "SELECT Nombre,Cedula,Origen,Destino,Hora,Fecha,Aerolinea,Precio\
     FROM VuelosClientes WHERE Fecha = %s"

    cursor = conexion.cursor()
    cursor.execute(bc, (Fecha,))

    datos2 = cursor.fetchall()
    
    datos = tk.StringVar()
    datos.set(datos2)

    t1 = tk.Text(nueva_ventana)
    t1.grid(row=2,
            column=0,
            sticky=tk.W,
            pady=4)
    for dtos in record:
        t1.insert(END, dtos)
        t1.insert(END, "\n")
        
    l1 = tk.Label(nueva_ventana, text="Registro con esta información:", bg="black", fg="red").grid(row=0,
      
                                                                                             column=0)
#    l2 = tk.Label(nueva_ventana, textvariable=datos).grid(row=1,
#                                                          column=0)


def ConsultarTodos():
    nueva_ventana = tk.Toplevel(marco)
    nueva_ventana.title("Consulta")
    nueva_ventana.geometry("800x400")
    nueva_ventana.configure(bg="black")

    def cierra_nueva():
        nueva_ventana.destroy()

    tk.Button(nueva_ventana, text="Cerrar", command=cierra_nueva, bg="black", fg="red").grid(row=2,
                                                                                             column=0,
                                                                                             sticky=tk.W,
                                                                                             pady=4)

    MostrarTablaMa = "select * from  VuelosClientes"
    cursor = conexion.cursor()
    cursor.execute(MostrarTablaMa)
    record = cursor.fetchall()

    
#    print(record)
    
    t1 = tk.Text(nueva_ventana)
    t1.grid(row=2,
            column=0,
            sticky=tk.W,
            pady=4)
    
    
#    contenido = str(record).split("}")
#    n = len(contenido)
#    i=0
#    while (i < n):
#        if contenido[i] == "}":
#            contenido = contenido.replace(contenido[i],"\n")
#            print(contenido)
#        i = i + 1
#    print(contenido)
#    t1.insert(END, contenido)
    
    for dtos in record:
        t1.insert(END, dtos)
        t1.insert(END, "\n")
        
        
    

    l1 = tk.Label(nueva_ventana, text="Registro Total:", bg="black", fg="red").grid(row=0,
                                                                                    column=0)
#    l2 = tk.Label(nueva_ventana, textvariable=datos).grid(row=1,
#                                                          column=0)


def cerrar():
    marco.destroy()


marco = tk.Tk()
marco.title("Consultar Clientes")
marco.geometry("500x400")
marco.configure(bg="black")


criterioCedula = tk.Entry(marco, width=20, bg="red", fg="black")
criterioCedula.grid(row=0, column=1, sticky=tk.W, pady=4)

criterioDestino = tk.Entry(marco, width=20, bg="red", fg="black")
criterioDestino.grid(row=1, column=1, sticky=tk.W, pady=4)

criterioAerolinea = tk.Entry(marco, width=20, bg="red", fg="black")
criterioAerolinea.grid(row=2, column=1, sticky=tk.W, pady=4)

criterioFecha = tk.Entry(marco, width=20, bg="red", fg="black")
criterioFecha.grid(row=3, column=1, sticky=tk.W, pady=4)


tk.Label(marco, text="Consultar tabla por Cedula", bg="black", fg="red").grid(row=0,
                                                                              column=0)

tk.Label(marco, text="Consultar tabla por Destino", bg="black", fg="red").grid(row=1,
                                                                               column=0)

tk.Label(marco, text="Consultar tabla por Aerolinea", bg="black", fg="red").grid(row=2,
                                                                                 column=0)

tk.Label(marco, text="Consultar tabla por Fecha", bg="black", fg="red").grid(row=3,
                                                                             column=0)

tk.Label(marco, text="Consultar Todos", bg="black", fg="red").grid(row=4,
                                                                   column=0)


tk.Button(marco, text="Consultar", command=EjecutarConsultaCedula, bg="black", fg="red").grid(row=0,
                                                                                              column=2,
                                                                                              sticky=tk.W,
                                                                                              pady=4, padx=4)

tk.Button(marco, text="Consultar", command=EjecutarConsultaDestino, bg="black", fg="red").grid(row=1,
                                                                                               column=2,
                                                                                               sticky=tk.W,
                                                                                               pady=4, padx=4)

tk.Button(marco, text="Consultar", command=EjecutarConsultaAerolinea, bg="black", fg="red").grid(row=2,
                                                                                                 column=2,
                                                                                                 sticky=tk.W,
                                                                                                 pady=4, padx=4)

tk.Button(marco, text="Consultar", command=EjecutarConsultaFecha, bg="black", fg="red").grid(row=3,
                                                                                             column=2,
                                                                                             sticky=tk.W,
                                                                                             pady=4, padx=4)

tk.Button(marco, text="Consultar", command=ConsultarTodos, bg="black", fg="red").grid(row=4,
                                                                                        column=2,
                                                                                        sticky=tk.W,
                                                                                        pady=4, padx=4)

tk.Button(marco, text="Cerrar", command=cerrar, bg="black", fg="red").grid(row=5,
                                                                           column=0,
                                                                           sticky=tk.W,
                                                                           pady=4,
                                                                           padx=45)

marco.mainloop()