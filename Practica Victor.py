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
     
      
  
            
 
