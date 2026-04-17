from math import pi
from time import sleep


def imprimir_hola_mundo():
    print("Hola Mundo!")


def saludar_usuario(nombre):
    print(f"Hola, {nombre}!")


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


def calcular_area_circulo(radio):

    area = pi * radio**2
    return round(area, 2)


def calcular_perimetro_circulo(radio):

    perimetro = 2 * pi * radio
    return round(perimetro, 2)


def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = round(a * b, 2)
    division = round(a / b, 2) if b != 0 else "No se puede dividir por cero"

    return (suma, resta, multiplicacion, division)


def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return round(imc, 2)


def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)


def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return round(promedio, 2)


def check_range(val, min_value, max_value, min_inclusive, max_inclusive, debug=False):
    if debug:
        print("min_value, max_value:")
        print(min_value, max_value)
        print("min_inclusive, max_inclusive:")
        print(min_inclusive, max_inclusive)
    min_check = True
    max_check = True
    if min_value is not None:
        if min_inclusive:
            if val < min_value:
                min_check = False
        else:
            if val <= min_value:
                min_check = False

    if max_value is not None:
        if max_inclusive:
            if val > max_value:
                max_check = False
        else:
            if val >= max_value:
                max_check = False

    return min_check and max_check


def abstract_negative_input(input_value):
    is_negative = input_value.startswith("-")
    return is_negative and input_value[1:] or input_value


def tool_rules_input(
    input_type="string",
    input_value="",
    min_value=None,
    max_value=None,
    debug=False,
    min_inclusive=True,
    max_inclusive=True,
):
    if debug:
        print(f"Validando entrada del tipo '{input_type}' con valor: '{input_value}'")
        print(f" - Valor mínimo: {min_value}")
        print(f" - Valor máximo: {max_value}")
    if input_type == "string":
        return input_value.isalpha()
    if input_type == "string_plus_space":
        return (
            all(part.isalpha() for part in input_value.split()) and len(input_value) > 0
        )
    if input_type == "alnum":
        return input_value.isalnum()
    if input_type == "alnum_plus_space":
        return (
            all(part.isalnum() for part in input_value.split()) and len(input_value) > 0
        )
    if input_type == "int":
        input_value_abstract = abstract_negative_input(input_value)
        if input_value_abstract.isdigit():
            val = int(input_value)
            return check_range(
                val=val,
                min_value=min_value,
                max_value=max_value,
                min_inclusive=min_inclusive,
                max_inclusive=max_inclusive,
                debug=debug,
            )
    if input_type == "float":
        input_value_abstract = abstract_negative_input(input_value)
        if input_value_abstract.count(".") == 0:
            if input_value_abstract.isdigit():
                return check_range(
                    val=float(input_value),
                    min_value=min_value,
                    max_value=max_value,
                    min_inclusive=min_inclusive,
                    max_inclusive=max_inclusive,
                    debug=debug,
                )
        elif input_value_abstract.count(".") == 1:
            integer_part, decimal_part = input_value_abstract.split(".")
            if not integer_part or not decimal_part:
                return False

            if integer_part.isdigit() and decimal_part.isdigit():
                val = float(input_value)
                return check_range(
                    val,
                    min_value,
                    max_value,
                    min_inclusive,
                    max_inclusive,
                    debug=debug,
                )
    return False


def tool_get_input(
    input_type="string",
    prompt="Ingrese un valor: ",
    prompt_error="Entrada inválida. Por favor, intente nuevamente.",
    min_value=None,
    max_value=None,
    debug=False,
    min_inclusive=True,
    max_inclusive=True,
):

    if debug:
        print(f"Validando entrada del tipo '{input_type}' con reglas:")
        print(f" - Valor mínimo: {min_value}")
        print(f" - Valor máximo: {max_value}")

    while True:
        user_input = input(prompt).strip()
        if tool_rules_input(
            input_type=input_type,
            input_value=user_input,
            min_value=min_value,
            max_value=max_value,
            debug=debug,
            min_inclusive=min_inclusive,
            max_inclusive=max_inclusive,
        ):
            if debug:
                print(f"Entrada válida: {user_input}")
            if user_input == "string":
                return user_input
            elif user_input == "string_plus_space":
                return user_input
            elif input_type == "alnum":
                return user_input
            elif input_type == "int":
                return int(user_input)
            elif input_type == "float":
                return float(user_input)
            return user_input
        print(prompt_error)


def print_lines_separator(middle_lines=40, upper_line_jump=False):
    if upper_line_jump:
        print()
    print("-" * middle_lines + "\n")


def print_menu():
    print("\nSeleccione una opción:")
    print("1. Imprimir 'Hola Mundo'")
    print("2. Saludar a un usuario")
    print("3. Mostrar información personal")
    print("4. Calcular área de un círculo")
    print("5. Calcular perímetro de un círculo")
    print("6. Mostrar tabla de multiplicar")
    print("7. Realizar operaciones básicas")
    print("8. Calcular IMC")
    print("9. Convertir Celsius a Fahrenheit")
    print("10. Calcular promedio de tres números")
    print("0. Salir")


def print_debug_info(*args):
    for arg in args:
        print(arg)


def init(debug=False):
    if debug:
        print("Modo debug activado.")

    is_program_running = True
    sleep_time = 1.5
    print("Bienvenido al programa de ejercicios. Seleccione una opción para continuar.")
    while is_program_running:
        print("Iniciando TP6 - Programación 1 - UTN - Vega Facundo")
        print_menu()
        print_lines_separator()
        if debug:
            print("Esperando entrada del usuario...")
            print_debug_info("Funciones disponibles:")
            print_debug_info(
                imprimir_hola_mundo,
                saludar_usuario,
                informacion_personal,
                calcular_area_circulo,
                calcular_perimetro_circulo,
                tabla_multiplicar,
                operaciones_basicas,
                calcular_imc,
                celsius_a_fahrenheit,
                calcular_promedio,
            )

        opcion = tool_get_input(
            input_type="int",
            prompt="Ingrese el número de la opción deseada: ",
            prompt_error="Opción inválida. Por favor, ingrese un número del 0 al 10.",
            min_value=0,
            max_value=10,
            debug=debug,
        )
        if debug:
            print(f"Opción seleccionada: {opcion}")
            print(opcion == 1)
        print_lines_separator()
        if opcion == 1:
            imprimir_hola_mundo()
        elif opcion == 2:
            nombre_usuario = tool_get_input(
                input_type="string_plus_space",
                prompt="Ingrese su nombre: ",
                prompt_error="Nombre inválido. Por favor, ingrese solo letras.",
                debug=debug,
            )
            saludar_usuario(nombre_usuario)
        elif opcion == 3:
            nombre = tool_get_input(
                input_type="string",
                prompt="Ingrese su nombre: ",
                prompt_error="Nombre inválido. Por favor, ingrese solo letras.",
                debug=debug,
            )
            apellido = tool_get_input(
                input_type="string",
                prompt="Ingrese su apellido: ",
                prompt_error="Apellido inválido. Por favor, ingrese solo letras.",
                debug=debug,
            )
            edad = tool_get_input(
                input_type="int",
                prompt="Ingrese su edad: ",
                prompt_error="Edad inválida. Por favor, ingrese un número.",
                debug=debug,
                min_value=0,
                min_inclusive=False,
            )
            residencia = tool_get_input(
                input_type="alnum_plus_space",
                prompt="Ingrese su lugar de residencia: ",
                prompt_error="Residencia inválida. Por favor, ingrese solo letras.",
                debug=debug,
            )
            informacion_personal(nombre, apellido, edad, residencia)
        elif opcion == 4:
            radio = tool_get_input(
                input_type="float",
                prompt="Ingrese el radio del círculo: ",
                prompt_error="Radio inválido. Por favor, ingrese un número real positivo.",
                debug=debug,
                min_value=0,
                min_inclusive=False,
            )

            area = calcular_area_circulo(radio)
            print(f"El área del círculo es: {area}")
        elif opcion == 5:
            radio = tool_get_input(
                input_type="float",
                prompt="Ingrese el radio del círculo: ",
                prompt_error="Radio inválido. Por favor, ingrese un número real positivo.",
                debug=debug,
                min_value=0,
                min_inclusive=False,
            )

            perimetro = calcular_perimetro_circulo(radio)
            print(f"El perímetro del círculo es: {perimetro}")
        elif opcion == 6:
            numero = tool_get_input(
                input_type="int",
                prompt="Ingrese un número para mostrar su tabla de multiplicar: ",
                prompt_error="Número inválido. Por favor, ingrese un número entero positivo.",
                debug=debug,
                min_value=0,
            )
            tabla_multiplicar(numero)

        elif opcion == 7:
            a = tool_get_input(
                input_type="float",
                prompt="Ingrese el primer número: ",
                prompt_error="Número inválido. Por favor, ingrese un número.",
                debug=debug,
            )
            b = tool_get_input(
                input_type="float",
                prompt="Ingrese el segundo número: ",
                prompt_error="Número inválido. Por favor, ingrese un número.",
                debug=debug,
            )
            resultados = operaciones_basicas(a, b)
            print(resultados)
            print(
                f"Suma: {resultados[0]}, Resta: {resultados[1]}, Multiplicación: {resultados[2]}, División: {resultados[3]}"
            )
        elif opcion == 8:
            peso = tool_get_input(
                input_type="float",
                prompt="Ingrese su peso en kg: ",
                prompt_error="Peso inválido. Por favor, ingrese un número positivo.",
                debug=debug,
                min_value=0,
            )

            altura = tool_get_input(
                input_type="float",
                prompt="Ingrese su altura en metros: ",
                prompt_error="Altura inválida. Por favor, ingrese un número.",
                debug=debug,
                min_value=0,
            )

            imc = calcular_imc(peso, altura)
            print(f"Su IMC es: {imc}")
        elif opcion == 9:
            celsius = tool_get_input(
                input_type="float",
                prompt="Ingrese la temperatura en Celsius: ",
                prompt_error="Temperatura inválida. Por favor, ingrese un número. Recuerde que la temperatura mínima en Celsius es -273.15.",
                debug=debug,
                min_value=-273.15,
            )
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius}°C es igual a {fahrenheit}°F")
        elif opcion == 10:
            num1 = tool_get_input(
                input_type="float",
                prompt="Ingrese el primer número: ",
                prompt_error="Número inválido. Por favor, ingrese un número.",
                debug=debug,
            )
            num2 = tool_get_input(
                input_type="float",
                prompt="Ingrese el segundo número: ",
                prompt_error="Número inválido. Por favor, ingrese un número.",
                debug=debug,
            )
            num3 = tool_get_input(
                input_type="float",
                prompt="Ingrese el tercer número: ",
                prompt_error="Número inválido. Por favor, ingrese un número.",
                debug=debug,
            )
            promedio = calcular_promedio(num1, num2, num3)
            print(f"El promedio de los números es: {promedio}")
        elif opcion == 0:
            print("Saliendo del programa. ¡Hasta luego!")
            is_program_running = False
            continue
        else:
            print("Opción no válida. Por favor, ingrese un número del 0 al 10.")

        print_lines_separator(upper_line_jump=True)

        sleep(sleep_time)


init(debug=False)
