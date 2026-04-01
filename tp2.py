def IsEithingYearsOld ():
    userYears = int(input("ingrese su edad"))
    if(userYears >= 18):
        print("Es mayor de edad")

def IsUserAproved():
    userNotes = int(input("Ingrese la nota"))
    if(userNotes >=6):
        print("Aprobado")
    else:
        print("Desaprobado")

def isNumberOdd ():
    userNumber = int(input("ingrese un numero"))
    while userNumber % 2 != 0:
        userNumber = int(input("Por favor, ingrese un número par"))
    print("Ha ingresado un número par")

def CheckUserYearsOld ():
    userYears = int(input("ingrese su edad"))
    if(userYears >= 0 and userYears < 12):
        print("niño/a")
    elif(userYears >= 12 and userYears < 18):
        print("adolecente")
    elif(userYears >= 18 and userYears < 30):
        print("Adulto/a joven")
    elif(userYears >= 30):
        print("Adulto/a")
        
def CreatePassword():
    newPassword = input("ingrese su contraseña")
    while len(newPassword) < 8 or len(newPassword) > 14:
        newPassword = input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    print("Ha ingresado una contraseña correcta")

def IsConsumeInWatt ():
    watts = int(input("consumo en kWh:"))
    if(watts >= 0 and watts < 150):
        print("Consumo bajo")
    elif(watts >= 150 and watts < 300):
        print("Consumo medio")
    elif(watts >= 300):
        print("Consumo alto")
        if watts > 500:
            print("Considere medidas de ahorro energético")

def EndsWithVowel():
    text = input("Ingrese una palabra o frase: ")
    if text[-1].lower() in "aeiou":
        print(text + "!")
    else:
        print(text)

def CostumeUserName ():
    userName = input("Ingrese su nombre")
    userOption = int(input("Ingrese la opcion 1, 2 o 3:"))
    if userOption == 1:
        print(userName.upper())
    elif userOption == 2:
        print(userName.lower())
    elif userOption == 3:
        print(userName.title())
    else:
        print("Opción incorrecta")


def EarthshakePrint ():
    magnitud = float(input("Ingrese la magnitud del terremoto:"))
    if(magnitud >= 0.0 and magnitud < 3.0):
        print("Muy leve")
    elif(magnitud >= 3.0 and magnitud < 4.0):
        print("leve")
    elif(magnitud >= 4.0 and magnitud < 5.0):
        print("moderado")
    elif(magnitud >= 5.0 and magnitud < 6.0):
        print("fuerte")
    elif(magnitud >= 6.0 and magnitud < 7.0):
        print("muy fuerte")
    else:
        print("extremo")

def PeriodOfYear ():
    day = int(input("ingrese el dia:"))
    month = int(input("ingrese el mes:"))
    zone = input("ingrese el si es del norte o sur N/S:").lower()
    season = ""
    if (month == 3 and day >= 21) or (month > 3 and month < 6) or (month == 6 and day <= 20):
        season = "primavera"
    elif (month == 6 and day >= 21) or (month > 6 and month < 9) or (month == 9 and day <= 20):
        season = "verano"
    elif (month == 9 and day >= 21) or (month > 9 and month < 12) or (month == 12 and day <= 20):
        season = "otoño"
    else:
        season = "invierno"

    if zone == "s":
        if season == "primavera":
            season = "otoño"
        elif season == "verano":
            season = "invierno"
        elif season == "otoño":
            season = "primavera"
        else:
            season = "verano"
    print(f"{season}")


