import os
import time
import csv

try:
    titulos = ["identificador","nombre","anio_lanzamiento"]
    with open("campeones_lol.csv","x",newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(titulos)
except:
    pass
while True:
    os.system('cls')
    print("MENU\n1. Agregar\n2. Ver\n3. Salir")
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in (1,2,3):
                break
            else:
                print("ERROR, la opcion que debe ingresar debe ser 1,2 o 3")
        except:
            print("La opcion debe ser ingresada en números enteros(1-2-3)")

    os.system('cls')
    if opc==1:    
        print("AGREGAR CAMPEÓN")
        while True:
            try:
                identificador = int(input("Ingrese identificador: "))
                if identificador >=1 and identificador <=158:
                    print("Identificador guardado!")
                    break
            except:
                print("Debe ingresar el identificador en números enteros!0}")
        while True:
            nombre = input("Ingrese nombre: ")
            if len(nombre)>=3 and len(nombre)<=14:
                print("Nombre guardado con extó")
                break
            else:
                print("Error, debe ser un campeon dispinible en el juego!")

        while True:
            try:
                nio = int(input("Ingrese año de lanzamiento: "))
                if nio >= 2009 and nio<=2024:
                    print("Año guardado con exitó")
                    break
                else:
                    print("Error,debe ingresar un año valido!")
            except:
                print("Debe ingresar los años en números (ejemplo=2011)")

        if identificador and nombre and nio:
            campeon_agregar = [identificador, nombre, nio]

            with open("campeones_lol.csv", "a", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(campeon_agregar)

            print("CAMPEÓN AGREGADO!")
        else:
            print("Error,No se pudo agregar el campeón, faltan datos")

    elif opc == 2:
        print("VER INFORMACIÓN")
        with open("campeones_lol.csv", "r", newline="") as archivo:
            lector = csv.reader(archivo)
            for campeon in lector:
                print(campeon)
        input("Presione Enter para continuar...")

    else:
        print("ADIOS!")
        break

    time.sleep(2)
