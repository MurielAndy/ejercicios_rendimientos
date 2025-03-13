import cProfile
import os


def letra_dni(dni):
    if len(str(dni)) != 8:
        raise Exception("El DNI debe tener 8 dígitos")
    LETRAS_DNI = 'TRWAGMYFPDXBNJZSQVHLCKE'
    return f"{dni}{LETRAS_DNI[int(dni) % 23]}"


def capitalizar(nombre):
    nombre=nombre.title()
   
    return nombre


def funcion50():

    csvModifikau=[]

    file = open("50.csv", 'r')
    lista = file.readlines()
    file.close()

    for linea in lista:
        linea = linea.replace("\n","").split(",")
        csvModifikau.append(capitalizar(linea[0])+","+letra_dni(linea[1])+"\n")
    
    file = open("Lista50.csv", 'w')
    file.writelines(csvModifikau)
    file.close()
    print("Fichero de 50 creado")

    return


def funcion1000():
    
    csvModifikau=[]

    file = open("1000.csv", 'r')
    lista = file.readlines()
    file.close()

    for linea in lista:
        linea = linea.replace("\n","").split(",")
        csvModifikau.append(capitalizar(linea[0])+","+letra_dni(linea[1])+"\n")
    
    file = open("Lista1000.csv", 'w')
    file.writelines(csvModifikau)
    file.close()
    print("Fichero de 1000 creado")
    return



while True:

    sel = int(input("Escribe numero de selección:\n1.Lista de 50\n2.Lista de 1000\n3.Borrar listas generadas \n-->"))
    
    if sel == 1:
        if os.path.exists("Lista50.csv"):
            os.remove("Lista50.csv")

        cProfile.run("funcion50()")

    elif sel == 2:
        if os.path.exists("Lista1000.csv"):
            os.remove("Lista1000.csv")

        cProfile.run("funcion1000()")
    
    elif sel == 3:
        if os.path.exists("Lista1000.csv"):
            os.remove("Lista1000.csv")
            print("Fichero de 1000 borrado")

        if os.path.exists("Lista50.csv"):
            os.remove("Lista50.csv")
            print("Fichero de 50 borrado")

        else:
            ""
            
        print("\n")
        
    
    else:
        print("introduce numero valido lol\n")
        