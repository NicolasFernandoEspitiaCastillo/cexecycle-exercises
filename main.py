#Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:

#Altura: 3
#Ancho: 5

#*****
#*****
#*****
#Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:

#Altura: 5

#*
#**
#***
#****
#*****
#Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:

#Lado: 4

#   ****
#  ******
# ********
#**********
# ********
#  ******
#   ****


#Programa para dibujar un rectangulo 

# Solicitar al usuario que ingrese la altura y el ancho del rectángulo
altura = int(input("Altura: "))
ancho = int(input("Ancho: "))

# Dibujar el rectángulo
for _ in range(altura):
    print('*' * ancho)


#Programa para dibujar un triangulo 

# Solicitar al usuario que ingrese la altura del triángulo
altura = int(input("Altura: "))

# Dibujar el triángulo
for i in range(1, altura + 1):
    print('*' * i)


#Programa para dibujar un hexagono

# Solicitar al usuario que ingrese el lado del hexágono
lado = int(input("Lado: "))

# Dibujar la parte superior del hexágono
for i in range(lado):
    print(' ' * (lado - i - 1) + '*' * (2 * i + 2))

# Dibujar la parte inferior del hexágono
for i in range(lado - 1):
    print(' ' * (i + 1) + '*' * (2 * (lado - i - 1) + 2))
