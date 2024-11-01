#El número de Euler, e ≈ 2,71828, puede ser representado como la siguiente suma infinita:

#e=10!+11!+12!+13!+14!+…
#Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.

#Recuerde que el factorial n! es el producto de los números de 1 a n.



# Función para calcular el factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Inicializar variables
n = 10
suma = 0.0
diferencia = float('inf')

# Calcular la suma hasta que la diferencia sea menor que 0.0001
while diferencia >= 0.0001:
    nuevo_termino = 1 / factorial(n)
    suma += nuevo_termino
    diferencia = nuevo_termino
    n += 1

# Imprimir el valor aproximado de e
print(f"Valor aproximado de e: {suma:.5f}")
