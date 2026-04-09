def create_list_studients_notes():
    studients = []
    for i in range(10):
        while True:
            name = input(f"Nombre del estudiante {i + 1}: ").strip().lower()
            if name and name.isalpha():
                break
            print(
                "El nombre no puede estar vacío y debe contener solo letras. Por favor, ingrese un nombre válido."
            )
        while True:
            note = input(f"Ingrese la nota del estudiante {i + 1}: ")
            if note.isdigit():
                note = int(note)
                if 0 <= note <= 10:
                    break
            print(
                "La nota no es válida. Por favor, ingrese un número entero entre 0 y 10."
            )
        studients.append({"name": name, "note": note})
    for studient in studients:
        print(f"{studient['name'].title()}: {studient['note']}")
    promedio = sum(studient["note"] for studient in studients) / len(studients)
    print(f"Promedio de notas: {promedio:.2f}")
    max_note_studient = max(studients, key=lambda s: s["note"])
    print(
        f"Estudiante con la nota más alta: {max_note_studient['name'].title()} con una nota de {max_note_studient['note']}"
    )
    min_note_studient = min(studients, key=lambda s: s["note"])
    print(
        f"Estudiante con la nota más baja: {min_note_studient['name'].title()} con una nota de {min_note_studient['note']}"
    )


def creat_list_product():
    products = []
    for i in range(5):
        while True:
            name = input(f"Enter the name of product {i + 1}: ").strip().lower()
            if name and name.isalpha():
                break
            print(
                "El nombre no puede estar vacío y debe contener solo letras. Por favor, ingrese un nombre válido."
            )

        products.append(name)
    for product in products:
        print(f"{product.title()}")

    while True:
        name = input(f"Ingrese el nombre del producto a eliminar: ").strip().lower()
        if name and name.isalpha():
            break
        print(
            "El nombre no puede estar vacío y debe contener solo letras. Por favor, ingrese un nombre válido."
        )
    if name in products:
        products.remove(name)
        print(f"Producto '{name.title()}' eliminado. Lista actualizada:")
        for product in products:
            print(f"{product.title()}")
    else:
        print(f"Producto '{name.title()}' no encontrado en la lista.")


def create_random_value_list():
    import random

    random_values = []
    random_values_odd = []
    random_values_even = []
    for _ in range(15):
        temp_value = random.randint(1, 100)
        random_values.append(temp_value)
        if temp_value % 2 == 0:
            random_values_even.append(temp_value)
        else:
            random_values_odd.append(temp_value)

    print("Valores aleatorios generados:")

    print(random_values)
    print()
    print("-" * 20)
    print()
    print(f"Cantidad de números pares: {len(random_values_even)}")
    print("Pares:")
    print(random_values_even)
    print()
    print("-" * 20)
    print()
    print(f"Cantidad de números impares: {len(random_values_odd)}")
    print("Impares:")

    print(random_values_odd)


def clean_list():
    datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
    cleaned_data = []
    for item in datos:
        if item not in cleaned_data:
            cleaned_data.append(item)

    print("Lista original:", datos)
    print("Lista limpia (sin duplicados):", cleaned_data)


def move_one_rigth():
    lista = [1, 2, 3, 4, 5, 6, 7]
    print("Lista original:", lista)
    first_element = ""
    if len(lista) > 1:
        for item, index in zip(lista, range(len(lista))):
            if index == 0:
                first_element = item
            if index < len(lista) - 1:
                lista[index] = lista[index + 1]
        lista[-1] = first_element
    print("Lista después de mover a la derecha:", lista)


def min_max_temperature():
    import random

    temperatures = []
    for i in range(7):
        min_temp = random.randint(-10, 15)
        max_temp = random.randint(min_temp + 5, 40)
        temperatures.append([min_temp, max_temp])

    print("Temperaturas registradas (mínima, máxima):")
    for [min_temp, max_temp] in temperatures:
        print(f"Temperatura mínima: {min_temp}°C, Temperatura máxima: {max_temp}°C")

    min_prom = 0
    max_prom = 0
    max_diff_index = 0

    for [min_temp, max_temp] in temperatures:
        min_prom += min_temp
        max_prom += max_temp
        if (
            max_temp - min_temp
            > temperatures[max_diff_index][1] - temperatures[max_diff_index][0]
        ):
            max_diff_index = temperatures.index([min_temp, max_temp])

    min_prom /= 7
    max_prom /= 7

    print(f"Promedio de temperaturas mínimas: {min_prom:.2f}°C")
    print(f"Promedio de temperaturas máximas: {max_prom:.2f}°C")
    print(
        f"Día con mayor diferencia entre temperatura mínima y máxima: {max_diff_index + 1} con una diferencia de {temperatures[max_diff_index][1] - temperatures[max_diff_index][0]}°C"
    )


def studient_list_notes():
    import random

    studients = []
    for i in range(5):
        first_note = random.randint(0, 10)
        second_note = random.randint(0, 10)
        third_note = random.randint(0, 10)
        studients.append([first_note, second_note, third_note])
    print("Notas de los estudiantes:")
    for index, notes in enumerate(studients):
        print(f"Estudiante {index + 1}: Notas: {notes}.")

    for index, notes in enumerate(studients):
        average = sum(notes) / len(notes)
        print(f"Promedio del estudiante {index + 1}: {average:.2f}")
    first_note_prom = sum(students[0] for students in studients) / len(studients)
    second_note_prom = sum(students[1] for students in studients) / len(studients)
    third_note_prom = sum(students[2] for students in studients) / len(studients)
    print(f"Promedio de la primera nota: {first_note_prom:.2f}")
    print(f"Promedio de la segunda nota: {second_note_prom:.2f}")
    print(f"Promedio de la tercera nota: {third_note_prom:.2f}")


def ta_te_ti():
    board = [["-" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print("Tablero:")
        for row in board:
            print("|".join(row))

        print(f"Jugador {current_player}, ingrese su movimiento: ")
        while True:
            while True:
                move_x = input("Ingrese fila(0-2): ")
                if move_x.isdigit() and move_x in ["0", "1", "2"]:
                    break
                print("Ingrese un valor para la fila entre 0 y 2.")
            while True:
                move_y = input("Ingrese columna(0-2): ")
                if move_y.isdigit() and move_y in ["0", "1", "2"]:
                    break
                print("Ingrese un valor para la columna entre 0 y 2.")
            if board[int(move_x)][int(move_y)] == "-":
                board[int(move_x)][int(move_y)] = current_player
                break
            print("La casilla ya está ocupada. Por favor, elija otra.")

        current_player = "O" if current_player == "X" else "X"
        print("-" * 20 + "\n")


def sales_of_week():
    import random

    sales_products = []
    for i in range(4):
        day_sales = []
        for j in range(7):
            sale = random.randint(0, 5)
            day_sales.append(sale)
        sales_products.append(day_sales)
    total_per_product = [0, 0, 0, 0]
    total_per_day = [0, 0, 0, 0, 0, 0, 0]
    for index, sales in enumerate(sales_products):
        for sale_index, sale in enumerate(sales):
            total_per_product[index] += sale
            total_per_day[sale_index] += sale
    most_product_sales_index = total_per_product.index(max(total_per_product))
    day_most_sales_index = total_per_day.index(max(total_per_day))
    print("Ventas por producto y día:")
    for index, sales in enumerate(sales_products):
        print(f"Producto {index + 1}: {sales}")

    print(
        f"Día con más ventas totales: Día {day_most_sales_index + 1} con {total_per_day[day_most_sales_index]} ventas."
    )
    print(
        f"Producto con más ventas totales: Producto {most_product_sales_index + 1} con {total_per_product[most_product_sales_index]} ventas."
    )


def ten_students_list():
    students = [
        "luis",
        "maria",
        "juan",
        "ana",
        "carlos",
        "laura",
        "pedro",
        "sofia",
        "diego",
        "valentina",
    ]
    for student in students:
        print(student.title())

    while True:
        name = input("Ingrese el nombre del estudiante a eliminar: ").strip().lower()
        if name and name.isalpha():
            break
        print(
            "El nombre no puede estar vacío y debe contener solo letras. Por favor, ingrese un nombre válido."
        )
    if name in students:
        index = students.index(name)
        print(
            f"Estudiante '{name.title()}' se encuentra en la lista en la posición {index}."
        )
    else:
        print(f"Estudiante '{name.title()}' no encontrado en la lista.")


def sorted_list():
    original_list = []
    for i in range(8):
        while True:
            value = input(f"Ingrese el valor {i + 1}: ")
            if value.isdigit():
                original_list.append(int(value))
                break
            print("Valor inválido. Por favor, ingrese un número entero.")

    print("Lista original:", original_list)
    original_list.sort()
    print("Lista ordenada:", original_list)
    original_list.sort(reverse=True)
    print("Lista ordenada de mayor a menor:", original_list)


def sort_pointed_list():
    puntajes = [450, 1200, 875, 990, 300, 1500, 640]

    most_indext = puntajes.index(max(puntajes))
    least_index = puntajes.index(min(puntajes))
    where_is_990 = puntajes.index(990)
    sorted_puntajes = sorted(puntajes, reverse=True)
    print("Puntajes originales:", puntajes)
    print(f"Puntaje más alto: {puntajes[most_indext]} en la posición {most_indext}")
    print(f"Puntaje más bajo: {puntajes[least_index]} en la posición {least_index}")
    print(f"Puntaje 990 se encuentra en la posición {where_is_990}")
    print("Puntajes ordenados de mayor a menor:", sorted_puntajes)
