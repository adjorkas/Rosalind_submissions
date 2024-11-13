# Ingresar 10 números enteros, calcular promedio e informar el máximo valor y su posición
valores = 10
contador = 1
suma, numero_actual, maximo, indice_max = 0, 0, 0, 0

while(contador <= valores):
    numero_actual = int(input("Ingresar número: "))
    suma = suma + numero_actual

    if numero_actual > maximo:
        maximo = numero_actual
        indice_max = contador

    contador = contador + 1

promedio = suma / valores
print(f"El promedio es {promedio}.")
print(f"El valor máximo es {maximo} y fue ingresado la vez número {indice_max}.")