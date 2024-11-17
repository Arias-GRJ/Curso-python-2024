# Solicitar el monto en pesos dominicanos
pesos = float(input("Introduce la cantidad en pesos dominicanos: "))

# Tasa de cambio aproximada
tasa_cambio = 0.018  # 1 peso dominicano = 0.018 dólares (esto puede variar)

# Calcular la cantidad en dólares
dolares = pesos * tasa_cambio

# Mostrar el resultado
print("El monto en dólares es: " + str(dolares))
