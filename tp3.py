def kioskoPurchase():

    name = input("Ingrese su nombre: ")
    while len(name) == 0 or not name.isalpha():
        print("El nombre no puede estar vacio y debe contener solo letras.")
        name = input("Ingrese su nombre nuevamente: ")

    while True:
        cantProducts = input("Ingrese la cantidad de productos que desea comprar: ")
        if cantProducts.isdigit() and int(cantProducts) > 0:
            cantProducts = int(cantProducts)
            break
        print("La cantidad de productos debe ser un numero entero positivo.")

    products = []
    for i in range(cantProducts):
        while True:
            price = input(f"Ingrese el precio del producto {i + 1}: ").strip()
            if price.isdigit() and int(price) > 0:
                price = int(price)
                break
            print("Debes ingresar un número entero mayor a 0")

        while True:
            isDiscount = input(f"¿El producto {i + 1} tiene descuento? (s/n): ").lower()
            if isDiscount in ["s", "n"]:
                break
            print("La respuesta debe ser 's' o 'n'.")

        products.append(
            {
                "name": f"Producto {i + 1}",
                "price": price,
                "discount": isDiscount,
            }
        )

    total = 0.0
    totalWithDiscount = 0.0
    saving = 0.0
    promedyCost = 0.0

    print(f"\nGracias por su compra, {name}!\nLos detalles a continuacion:")
    print(f"Producto comprados: {len(products)}")
    print("\nResumen de la compra:")
    for product in products:
        print(
            f"- {product['name']}: ${product['price']:.2f} (Descuento: {product['discount']})"
        )

        tempPrice = float(product["price"])
        tempDiscount = 0.9 if product["discount"] == "s" else 1.0

        total += tempPrice
        totalWithDiscount += tempPrice * tempDiscount
        saving += tempPrice * (1 - tempDiscount)
        promedyCost = totalWithDiscount / int(cantProducts)

    print(f"\nTotal sin descuento: ${total:.2f}")
    print(f"Total con descuento: ${totalWithDiscount:.2f}")
    print(f"Total ahorrado: ${saving:.2f}")
    print(f"Promedio de costo por producto: ${promedyCost:.2f}")


def loginUserAndMenu():

    state = {
        "username": "alumno",
        "password": "python123",
        "attempts": 3,
        "login": False,
    }

    def changePassword():
        while True:
            newPassword = input("Ingrese la nueva clave: ")
            if len(newPassword) >= 6:
                state["password"] = newPassword
                print("Clave cambiada exitosamente.")
                break
            print("La clave debe tener al menos 6 caracteres.")

    def logOut():
        print("Cerrando sesión...")
        state["login"] = False
        return

    while True:
        while state["attempts"] > 0:
            print('Ingrese usuario "0" para salir: ')
            username = input("Ingrese su nombre de usuario: ")
            if username == "0":
                print("Saliendo del programa...")
                return
            password = input("Ingrese su contraseña: ")

            if username == state["username"] and password == state["password"]:

                print(f"Bienvenido, {username}!")
                state["attempts"] = 3
                state["login"] = True
                break
            else:
                state["attempts"] -= 1
                print(
                    f"Credenciales incorrectas. Intentos restantes: {state['attempts']}"
                )

        if state["attempts"] <= 0:
            print("Cuenta bloqueada.")
            return

        menuActions = {
            "1": lambda: print("Estado de inscripción: Inscrito"),
            "2": changePassword,
            "3": lambda: print("¡Sigue adelante, estás haciendo un gran trabajo!"),
            "4": logOut,
        }

        while state["login"]:
            print("\n--- Menú ---")
            print("1. Estado de inscripción")
            print("2. Cambiar clave")
            print("3. Mostrar mensaje motivacional")
            print("4. Salir")
            choice = input("Seleccione una opción: ")
            if choice not in menuActions:
                print("Opción no válida")
                continue

            menuActions[choice]()


def crudTurns():
    isMondayAvailable = True
    mondayTurn1 = ""
    mondayTurn2 = ""
    mondayTurn3 = ""
    mondayTurn4 = ""

    isTuesdayAvailable = True
    tuesdayTurn1 = ""
    tuesdayTurn2 = ""
    tuesdayTurn3 = ""

    while True:
        print("\n--- Menú de Turnos ---")
        print("1. Reservar turno")
        print("2. Cancelar turno")
        print("3. Ver turnos disponibles")
        print("4. Ver resumen general")
        print("5. Salir")
        choice = input("Seleccione una opción: ")

        match choice:

            case "1":
                while True:
                    day = input(
                        "Ingrese el día para reservar Lunes(1) o Martes(2) o 0 para salir: "
                    )
                    if day == "1" or day == "2" or day == "0":
                        break
                    print(
                        "Día no válido, por favor ingrese '1' para Lunes o '2' para Martes o 0 para salir."
                    )

                if day == "1":
                    if not isMondayAvailable:
                        print("No hay turnos disponibles para el lunes.")
                        continue
                    while True:
                        name = input(
                            "Ingrese su nombre para el turno del lunes: "
                        ).lower()
                        if name.isalpha() and len(name) > 0:
                            print(f"Agendando turno a {name}.")
                            break
                        print(
                            "El nombre debe contener solo letras y no puede estar vacío."
                        )
                    turn = ""
                    if (
                        mondayTurn1 == name
                        and (turn := "1")
                        or mondayTurn2 == name
                        and (turn := "2")
                        or mondayTurn3 == name
                        and (turn := "3")
                        or mondayTurn4 == name
                        and (turn := "4")
                    ):

                        print(
                            f"{name}, ya tiene un turno {turn} reservado para el lunes."
                        )
                        continue
                    elif not mondayTurn1:
                        mondayTurn1 = name
                        turn = "1"
                    elif not mondayTurn2:
                        mondayTurn2 = name
                        turn = "2"

                    elif not mondayTurn3:
                        mondayTurn3 = name
                        turn = "3"
                    elif not mondayTurn4:
                        mondayTurn4 = name
                        turn = "4"
                    print(f"{name}, turno lunes número {turn}.")
                    if mondayTurn1 and mondayTurn2 and mondayTurn3 and mondayTurn4:
                        isMondayAvailable = False
                elif day == "2":
                    if not isTuesdayAvailable:
                        print("No hay turnos disponibles para el martes.")
                        continue
                    while True:
                        name = input(
                            "Ingrese su nombre para el turno del Martes: "
                        ).lower()
                        if name.isalpha() and len(name) > 0:
                            print(f"Agendando turno a {name}.")
                            break
                        print(
                            "El nombre debe contener solo letras y no puede estar vacío."
                        )
                    turn = ""
                    if (
                        tuesdayTurn1 == name
                        and (turn := "1")
                        or tuesdayTurn2 == name
                        and (turn := "2")
                        or tuesdayTurn3 == name
                        and (turn := "3")
                    ):
                        print(
                            f"{name}, ya tienes un turno {turn} reservado para el martes."
                        )
                        continue
                    elif not tuesdayTurn1:
                        turn = "1"
                        tuesdayTurn1 = name
                    elif not tuesdayTurn2:
                        tuesdayTurn2 = name
                        turn = "2"

                    elif not tuesdayTurn3:
                        tuesdayTurn3 = name
                        turn = "3"

                    print(f"{name}, turno martes número {turn}.")
                    if tuesdayTurn1 and tuesdayTurn2 and tuesdayTurn3:
                        isTuesdayAvailable = False
                else:
                    print("Saliendo al menú principal...")

            case "2":
                while True:
                    day = input(
                        "Ingrese el día para cancelar el turno Lunes(1) o Martes(2) o 0 para salir: "
                    )
                    if day == "1" or day == "2" or day == "0":
                        break
                    print(
                        "Día no válido, por favor ingrese '1' para Lunes o '2' para Martes."
                    )
                while True:
                    name = input("Ingrese su nombre: ").lower()
                    if name.isalpha() and len(name) > 0:
                        break
                    print("El nombre debe contener solo letras y no puede estar vacío.")
                turn = ""
                if day == "1":
                    if mondayTurn1 == name:
                        mondayTurn1 = ""
                        turn = "1"
                        isMondayAvailable = True
                    elif mondayTurn2 == name:
                        mondayTurn2 = ""
                        turn = "2"
                        isMondayAvailable = True
                    elif mondayTurn3 == name:
                        mondayTurn3 = ""
                        turn = "3"
                        isMondayAvailable = True
                    elif mondayTurn4 == name:
                        mondayTurn4 = ""
                        turn = "4"
                        isMondayAvailable = True
                    else:
                        print("No tienes un turno reservado para el lunes.")
                        continue

                    print(f"{name}, turno lunes número {turn} cancelado.")
                elif day == "2":
                    if tuesdayTurn1 == name:
                        tuesdayTurn1 = ""
                        turn = "1"
                        isTuesdayAvailable = True
                    elif tuesdayTurn2 == name:
                        tuesdayTurn2 = ""
                        turn = "2"
                        isTuesdayAvailable = True
                    elif tuesdayTurn3 == name:
                        tuesdayTurn3 = ""
                        turn = "3"
                        isTuesdayAvailable = True
                    else:
                        print("No tienes un turno reservado para el martes.")
                        continue
                    print(f"{name}, turno martes número {turn} cancelado.")
                else:
                    print("Saliendo al menú principal...")

            case "3":
                print("\n--- Turnos Disponibles ---")
                day = ""
                while True:
                    day = input("Ingrese el día para reservar Lunes(1) o Martes(2): ")
                    if day == "1" or day == "2" or day == "0":
                        break
                    print(
                        "Día no válido, por favor ingrese '1' para Lunes o '2' para Martes. 0 para salr"
                    )

                if day == "1":
                    print(
                        f"Lunes: 1_{mondayTurn1 or "libre"}, 2_{mondayTurn2 or "libre"}, 3_{mondayTurn3 or "libre"}, 4_{mondayTurn4 or "libre"}"
                    )
                elif day == "2":
                    print(
                        f"Martes: 1_{tuesdayTurn1 or "libre"}, 2_{tuesdayTurn2 or "libre"}, 3_{tuesdayTurn3 or "libre"}"
                    )
                else:
                    print("Saliendo al menú principal...")

            case "4":
                print("\n--- Resumen General ---")
                print(
                    f"Lunes: 1_{mondayTurn1 or "libre"}, 2_{mondayTurn2 or "libre"}, 3_{mondayTurn3 or "libre"}, 4_{mondayTurn4 or "libre"}"
                )
                print(
                    f"Martes: 1_{tuesdayTurn1 or "libre"}, 2_{tuesdayTurn2 or "libre"}, 3_{tuesdayTurn3 or "libre"}"
                )

            case "5":
                print("Saliendo del programa...")
                break

            case _:
                print("Opción no válida, por favor intente nuevamente.")


def escapeRoomLaBoveda():
    defaultState = {
        "energy": 100,
        "time": 12,
        "openLocks": 0,
        "alarm": False,
        "tempCode": "",
        "locksAttemptsRemaining": 3,
        "name": "",
    }

    state = {
        "energy": defaultState["energy"],
        "time": defaultState["time"],
        "openLocks": defaultState["openLocks"],
        "alarm": defaultState["alarm"],
        "tempCode": defaultState["tempCode"],
        "locksAttemptsRemaining": defaultState["locksAttemptsRemaining"],
        "name": "",
    }

    locksAction = {
        "energy": -20,
        "time": -2,
    }

    hackAction = {
        "energy": -10,
        "time": -3,
    }

    waitAction = {
        "energy": 15,
        "time": -1,
    }

    while True:
        state["name"] = input("Ingrese su nombre: ")
        if state["name"].isalpha() and len(state["name"]) > 0:
            print(f"Bienvenido, {state['name']}!")
            break
        print("El nombre debe contener solo letras y no puede estar vacío.")

    def validateGame():
        if len(state["tempCode"]) >= 8:
            state["openLocks"] += 1
            state["tempCode"] = ""
            print(
                f"¡Código de seguridad correcto, {state['name']}! Has abierto una cerradura."
            )
        if state["openLocks"] >= 3:
            print(
                f"¡Felicidades, {state['name']}! Has abierto las 3 cerraduras y escapaste de la boveda."
            )
            return True
        if state["energy"] <= 0 or state["time"] <= 0:
            print(
                f"Lo siento, {state['name']}. Has perdido toda tu energía o se te ha acabado el tiempo. ¡Game Over!"
            )
            return True
        if state["alarm"] and state["time"] <= 3 and state["openLocks"] < 3:
            print(
                f"¡Alarma activada, {state['name']}! Has sido atrapado por los guardias. ¡Game Over!"
            )
            return True
        return False

    while not validateGame():
        print("\n--- Menú de Acciones ---")
        print("1. Intentar abrir una cerradura")
        print("2. Intentar hackear el sistema de seguridad")
        print("3. Esperar para recuperar energía")
        print(f"E: {state['energy']}, T: {state['time']}, C: {state['openLocks']}")
        choice = input("Seleccione una acción: ")

        match choice:
            case "1":
                state["energy"] += locksAction["energy"]
                state["time"] += locksAction["time"]
                state["locksAttemptsRemaining"] -= 1
                if state["locksAttemptsRemaining"] <= 0:
                    print(
                        "Has agotado tus intentos para abrir cerraduras, la alarma se ha activado!"
                    )
                    state["alarm"] = True
                    continue
                if state["alarm"]:
                    print("Las alarmas te impiden forzar la cerradura")
                    continue
                if state["energy"] <= 0 or state["time"] <= 0:
                    print(
                        "No tienes suficiente energía o tiempo para abrir la cerradura."
                    )
                    continue
                if state["energy"] < 40:
                    print("Cuidado alarma")
                    setOff = input(
                        "Ingrese un algun digito del 1, 2 o 3 para desactivar la alarma: "
                    )
                    if (
                        setOff.isdigit()
                        and len(setOff) == 1
                        and setOff in ["1", "2", "3"]
                    ):
                        if setOff == "3":
                            print("Escuchas las sirenas de alarmas")
                            state["alarm"] = True
                            continue
                        print("Has evitado que se active la alarma")
                    else:
                        print("Entrada no válida, la alarma se ha activado.")
                        state["alarm"] = True
                        continue

                state["openLocks"] += 1
                print(
                    f"Has abierto una cerradura! Cerraduras abiertas: {state['openLocks']}"
                )

            case "2":
                state["energy"] += hackAction["energy"]
                state["time"] += hackAction["time"]
                state["locksAttemptsRemaining"] = defaultState["locksAttemptsRemaining"]
                for i in range(4):
                    temp = input("Ingrese una letra del código de seguridad: ")
                    if len(temp) != 1:
                        print("ERROR")
                        continue
                    state["tempCode"] += temp
            case "3":

                state["energy"] = max(
                    0,
                    min(
                        100,
                        (
                            state["energy"]
                            + waitAction["energy"]
                            + (-10 if state["alarm"] else +0)
                        ),
                    ),
                )

                state["time"] = max(0, state["time"] + min(0, waitAction["time"]))
                state["locksAttemptsRemaining"] = defaultState["locksAttemptsRemaining"]
                print("Has esperado un momento y recuperado algo de energía.")
            case _:
                print("Opción no válida, por favor intente nuevamente.")


def escapeRoomGladiatorArena():

    baseDamages = {
        "fast": 5,
        "normal": 12,
        "heavy": 15,
    }

    defaultPlayerState = {
        "hp": 100,
        "name": "",
        "heavyDamage": baseDamages["heavy"],
        "fastDamage": baseDamages["fast"],
        "lifePotions": 3,
        "active": False,
    }

    defaultGladiatorState = {
        "name": "",
        "hp": 100,
        "normalDamage": baseDamages["normal"],
        "active": False,
    }
    playerState = defaultPlayerState.copy()
    gladiatorState = defaultGladiatorState.copy()
    while True:
        playerState["name"] = input("Ingrese su nombre: ")
        if playerState["name"].isalpha() and len(playerState["name"]) > 0:
            print(f"Bienvenido, {playerState['name']}!")
            break
        print("El nombre debe contener solo letras y no puede estar vacío.")

    playerState["active"] = True
    print(f"A comenzado el combate entre {playerState['name']} y un gladiador anonimo")

    def isCombatActive():
        if playerState["hp"] <= 0:
            print("-" * 20)
            print("DERROTA. Has caído en combate.")
            return False
        if gladiatorState["hp"] <= 0:
            print("-" * 20)
            print(f"¡VICTORIA! {playerState['name']} ha ganado la batalla.")
            return False
        return True

    turn = 0
    while isCombatActive():
        print("-" * 20)
        turn += 1
        print(f"Turno: {turn}")
        print(
            f"{playerState['name']} HP: {playerState['hp']} vs Gladiador Anonimo HP: {gladiatorState['hp']}"
        )
        print(f"Pociones: {playerState['lifePotions']}")
        if playerState["active"]:

            print("Tu turno, elija entre las opciones su accion")
            print("1.Ataque Pesado")
            print("2.Ráfaga Veloz")
            print("3.Usar poción")
            while True:
                choise = input("Ingrese su accion: ")
                if choise.isdigit() and choise in ["1", "2", "3"]:
                    break
                print("Ingrese una accion valida 1, 2 o 3")
            match choise:
                case "1":

                    totalDamage = playerState["heavyDamage"]
                    if gladiatorState["hp"] < 20:
                        totalDamage = int(totalDamage * 1.5)

                    gladiatorState["hp"] = max(0, gladiatorState["hp"] - totalDamage)
                    print(f"¡Atacaste al enemigo por {totalDamage} puntos de daño!")
                case "2":
                    for _ in range(3):
                        totalDamage = playerState["fastDamage"]
                        gladiatorState["hp"] = max(
                            0, gladiatorState["hp"] - totalDamage
                        )
                        print(f"> Golpe conectado por {totalDamage} de daño")
                        if gladiatorState["hp"] <= 0:
                            break

                case "3":
                    if playerState["lifePotions"] <= 0:
                        print("¡No quedan pociones!")
                    else:
                        playerState["lifePotions"] -= 1
                        playerState["hp"] = min(100, playerState["hp"] + 30)
                        print(f"Te curaste 30 HP. Vida actual: {playerState['hp']}")
            playerState["active"] = not playerState["active"]
            gladiatorState["active"] = not gladiatorState["active"]
            continue
        if gladiatorState["active"]:
            print("Turno del gladiador anonimo")
            playerState["hp"] = max(
                0, playerState["hp"] - gladiatorState["normalDamage"]
            )

            print(
                f"¡El enemigo te atacó por {gladiatorState['normalDamage']} puntos de daño!"
            )
            playerState["active"] = not playerState["active"]
            gladiatorState["active"] = not gladiatorState["active"]
            continue
