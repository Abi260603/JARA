import math

# Definición de funciones
def suma():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"El resultado de la suma es: {num1 + num2}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

def producto():
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print(f"El resultado del producto es: {num1 * num2}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

def division():
    try:
        num1 = float(input("Ingrese el numerador: "))
        num2 = float(input("Ingrese el denominador: "))
        if num2 == 0:
            print("La división por cero no está permitida.")
else:
print(f"El resultado de la division es:{num1 / num2}")
except ValueError:
print("Por favor, ingrese valores numéricos válidos.")

def factorial():
    try:
        num = int(input("ingrese un numero para calcular su factorial:"))
        if num < 0:
            print("El factorial no esta definido para numeros negativos:")
        else:
            resultado = math.factorial(num)
            print(f"El factorial de {num} es: {resultado}")
    except ValueError:
        print("Por favor, ingrese un numero valido.")
 
def tabla_multiplicar():
    try:
        num = int(input("Seleccione la tabla de multiplicar (1 al 10):"))
        if 1 <= num <=10:
            for i in range(1,11):
                print(f"{num} x {i} = {num * i}")
        else:
            print("Por favor, seleccione un numero entre 1 y 10.")
    except ValueError:
        print("Por favor, ingrese un numero entero valido.")

def calcular_potencia():
    try:
        opcion = int(input("Seleccione: 1 para cuadrado, 2 para cubo."))
        if opcion in [1,2]:
            num = float(input("Ingrese el numero:"))
            exponente = 2 if opcion == 1 else 3
            print(f"El resultado de {num}^{exponente} es: {math.pow(num,exponente)}")

else:
print("Por favor, seleccione una opcion valida.")
            except ValueError:
print("Por favor, ingrese valores numericos validos.")

def calcular_media():
    try:
        cantidad = int(input("ingrese la cantidad de numeros:"))
        if cantidad <= 0:
            print("La cantidad debe ser un numero positivo.")
            return
            suma = 0
            for _ in range(cantidad):
                while True:
                    try:
                        numero = float(input("ingrese un numero:"))
                        suma += numero
                        break
                    except ValueError:
                        print("Ingrese un numero valido.")
                        print(f"La media es: {suma / cantidad}")
                    except ValueError:
                        print("Por favor, ingrese un numero entero valido.")

def ordenar_numeros():
    try:
        cantidad = int(input("Ingrese la cantidad de numeros a ordenar:"))
        if cantidad <= 0:
            print("La cantidad debe ser un numero positivo.")
            return
            numeros = []
            for _ in range(cantidad):
                while True:
                    try:
                        
            
     
      
  
            
 
