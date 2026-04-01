def sayHelloWord():
    print("Hello World")

def salute():
    name = input("Cual es su nombre? ")
    print(f"Hola {name}!")

def saluteFullData():
    name = input("Cual es su nombre? ")
    surname = input("Cual es su apellido? ")
    old= input("Cual es su edad? ")
    country = input("Cual es su pais? ")
    print(f"soy {name} {surname}, tengo {old} años y vivo en {country}!")

def calculateCircleAreaPerimeter():
    tempPi = 3.14
    radio = float(input("Ingrese el radio del circulo: "))
    area = tempPi * radio ** 2
    perimetro = 2 * tempPi * radio
    print(f"El area del circulo es: {area:.2f}")
    print(f"El perimetro del circulo es: {perimetro:.2f}")


def calculateSecondsToHours():
    seconds = int(input("Ingrese la cantidad de segundos: "))
    hours = seconds / 3600
    print(f"{seconds} segundos son equivalentes a {hours:.2f} horas.")

def multiplicationTable():
    number = int(input("Ingrese un numero: "))
    print(f"Tabla de multiplicar del {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}") 

def basicOperations():
    num1 = float(input("Ingrese el primer numero: "))
    while(num1 == 0):
        print("El primer numero no puede ser cero.")
        num1 = float(input("Ingrese el primer numero: "))
        return
    num2 = float(input("Ingrese el segundo numero: "))
    while(num2 == 0):
        print("El segundo numero no puede ser cero.")
        num2 = float(input("Ingrese el segundo numero: "))
        return
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicacion: {multiplicacion}")
    print(f"Division: {division}")

def calculateIMC():
    weight = float(input("Ingrese su peso en kg: "))
    height = float(input("Ingrese su altura en metros: "))
    imc = weight / (height ** 2)
    print(f"Su indice de masa corporal (IMC) es: {imc:.2f}")

def celciusToFahrenheit():
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados Celsius son equivalentes a {fahrenheit:.2f} grados Fahrenheit.")

def promedyOfThree():
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    num3 = float(input("Ingrese el tercer numero: "))
    average = (num1 + num2 + num3) / 3
    print(f"El promedio de los tres numeros es: {average:.2f}")
