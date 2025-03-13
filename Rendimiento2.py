import datetime

def fibonacci_r(n):
    if n <= 0:
        print("El número debe ser un numero entero positivo")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci_r(n-1) + fibonacci_r(n-2)

def fibonacci_b(n):
    A = 0
    B = 1
    for i in range(n-1):
        C = A + B
        A = B
        B = C
    return C

while True:
    
    n = int(input("Introduce un número de sucesiones: "))
    sel = int(input("Escribe numero de selección:\n1.Por recursividad\n2.Por bubcles\n-->"))
    
    if sel == 1:
        start_time = datetime.datetime.now()
        print("El valor de fibonnaci para la sucesion nº:",n,"es:",fibonacci_r(n))
        end_time = datetime.datetime.now()
        print("El tiempo de ejecución es:", end_time - start_time,"\n")

    elif sel == 2:
        start_time = datetime.datetime.now()
        print("El valor de fibonnaci para la sucesion nº:",n,"es:",fibonacci_b(n))
        end_time = datetime.datetime.now()
        print("El tiempo de ejecución es:", end_time - start_time,"\n")

    else:
        print("introduce un numero valido")