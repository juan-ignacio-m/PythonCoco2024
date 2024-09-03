#Se pide crear un programa que dada la longitud del lado 
#de un cuadrado (L) se calcule el perímetro, y su área.
#Luego, evolucione su programa hecho anteriormente para que pueda
#calcular con ese mismo dado el volumen de un cubo de la L.
#Adjuntar solo el archivo.py que resuelva el problema.

# cuadrado_y_cubo.py

# Solicitar la longitud del lado del cuadrado al usuario
lado = float(input("Introduce la longitud del lado del cuadrado: "))

# Calcular el perímetro del cuadrado
perimetro = 4 * lado

# Calcular el área del cuadrado
area = lado * lado

# Calcular el volumen del cubo
volumen = lado * lado * lado

# Mostrar los resultados
print("El perímetro del cuadrado es:", perimetro)
print("El área del cuadrado es:", area)
print("El volumen del cubo es:", volumen)