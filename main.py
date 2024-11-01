#Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos. Por ejemplo, si los números son 1 y 7, 
# debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.

#Ingrese num: 1
#Ingrese num: 7
#La suma es 20


# Solicitar al usuario que ingrese dos números enteros
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Asegurar que num1 sea el menor y num2 el mayor
if num1 > num2:
    num1, num2 = num2, num1

# Calcular la suma de los números entre num1 y num2
suma = sum(range(num1 + 1, num2))

# Mostrar el resultado
print(f"La suma es {suma}")
