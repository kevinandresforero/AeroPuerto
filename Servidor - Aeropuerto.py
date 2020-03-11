import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import socket


def main():

    IP = "10.20.150.122"
    PORT = 1234

    based = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Dragon",
            database="aeropuerto")
    
    micursor = based.cursor()
    # micursor.execute("CREATE DATABASE aeropuerto")

    micursor.execute("DROP TABLE IF EXISTS clientes")

    micursor.execute("CREATE TABLE clientes(Nombre VARCHAR(100), Cedula INT(10) PRIMARY KEY,\
        Origen VARCHAR(100), Destino VARCHAR(100), Hora VARCHAR(5),\
        Fecha VARCHAR(10), Aerolinea VARCHAR(50), Costo INT(10))")
    
    micursor.close()
    based.close()

    op = 0

    while op != 6:

        print("1. Registrar cliente")
        print("2. Listar tabla")
        print("3. Consultar por origen")
        print("4. Consultar por origen")
        print("5. Retirar un cliente")
        print("6. Termina")

        op = int(input("Digite opcion: "))

        if op is 1:
            based = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Dragon",
                database="aeropuerto")

            micursor = based.cursor()

            print("Inserte un cliente")
            ced = int(input("Cedula: "))

            # chequea si el estudiante ya existe...
            sql_select1 = "select * from clientes\
                    where cedula=%s"
            # tupla con 1 elemento
            micursor.execute(sql_select1, (ced,))
            micursor.fetchone()
            if micursor.rowcount > 0:
                print("Ya existe el cliente con la cedula: " + str(ced))
                micursor.close()
                based.close()
            else:
                nom = input("Nombre: ")
                ori = input("Origen: ")
                des = input("Destino: ")
                hor = input("Hora: ")
                fec = input("Fecha: ")
                aer = input("Aerolinea: ")
                cos = int(input("Costo: "))

                sqlIn = "insert into clientes(\
                    Nombre,Cedula,Origen,Destino,Hora,Fecha,Aerolinea,Costo) \
                    values(%s,%s,%s,%s,%s,%s,%s,%s)"
                micursor.execute(sqlIn, (nom, ced, ori, des, hor, fec, aer, cos))
                based.commit()
                micursor.close()
                based.close()

                print("Insertado registro")


if __name__ == "__main__":
    main()
