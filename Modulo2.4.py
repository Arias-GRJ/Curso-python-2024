# Inicializar la suma de notas y el contador de notas
suma = 0
cantidad = int(input("¿Cuántas notas quieres ingresar? "))

# Solicitar las notas y calcular la suma
for i in range(cantidad):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    suma += nota

# Calcular el promedio
promedio = suma / cantidad

# Mostrar el resultado
print("El promedio es:", promedio)
