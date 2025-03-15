import time
import datetime
import cProfile

def fibonacci_recursivo(n):
    """Calcula el número de Fibonacci de forma recursiva."""
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_iterativo(n):
    """Calcula el número de Fibonacci de forma iterativa."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def factorial_recursivo(n):
    """Calcula el factorial de un número de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)

def factorial_iterativo(n):
    """Calcula el factorial de un número de forma iterativa."""
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


valores_n = [10, 20, 30, 40, 50]


def medir_tiempo(func, n):
    start_time = datetime.datetime.now()
    resultado = func(n)
    end_time = datetime.datetime.now()
    return resultado, (end_time - start_time).total_seconds()


for n in valores_n:
    print(f"Calculando para n = {n}...")
    
    
    if n <= 30:
        resultado_fib_rec, tiempo_fib_rec = medir_tiempo(fibonacci_recursivo, n)
    else:
        resultado_fib_rec, tiempo_fib_rec = "No calculado", "N/A"

    
    resultado_fib_iter, tiempo_fib_iter = medir_tiempo(fibonacci_iterativo, n)

    
    resultado_fac_rec, tiempo_fac_rec = medir_tiempo(factorial_recursivo, n)

    
    resultado_fac_iter, tiempo_fac_iter = medir_tiempo(factorial_iterativo, n)

    
    print(f"  Fibonacci Recursivo: {resultado_fib_rec}, Tiempo: {tiempo_fib_rec} s")
    print(f"  Fibonacci Iterativo: {resultado_fib_iter}, Tiempo: {tiempo_fib_iter} s")
    print(f"  Factorial Recursivo: {resultado_fac_rec}, Tiempo: {tiempo_fac_rec} s")
    print(f"  Factorial Iterativo: {resultado_fac_iter}, Tiempo: {tiempo_fac_iter} s")
    print("---------------------------------------------------")


print("\nPerfilando Fibonacci Iterativo con cProfile para n=30")
cProfile.run("fibonacci_iterativo(30)")
