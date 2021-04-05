from Users import New_Users
from Rooms import Rooms
import time
import operator

#Función para verificar si el Nombre de Usuario existe:
def check_user_name (user_name):
    taken_user_names = []
    with open ("Users_Database.txt") as users_database:
        users_info = users_database.readlines()
    for users_and_passwords in users_info:
        user_and_password = users_and_passwords[:-1].split(":")
        taken_user_names.append(user_and_password[0])
    if user_name in taken_user_names:
        return True
    else:
        return False

#Función para validar que la Contraseña corresponda con el Nombre de Usuario:
def check_password (user_name, password):
    with open ("Users_Database.txt", "r") as users_database:
        users_info = users_database.readlines()
    for users_and_passwords in users_info:
        user_and_password = users_and_passwords[:-1].split(":")
        for user_name in user_and_password:
            if user_name == user_and_password[0]:
                if password == user_and_password[1]:
                    return True

#Función para validar si el formato del Nombre de Usuario es correcto al momento de registrarse:
def ok_user_name (user_name):
    while (user_name.isnumeric() or check_user_name(user_name) or not user_name.isalnum()):
        user_name = input("""
    Nombre de Usuario inválido, ingrese un Nombre de Usuario diferente: """)
    return user_name

#Función para validar si el formato de la Contraseña es correcto al momento de registrarse
def ok_password (password):
    while (len(password) < 8 or not password.isalnum()):
        password = input("""
    Contraseña inválida, asegurese de que su contraseña contenga al menos 8 caracteres y no contenga espacios: """)
    return password

#Función para validar la edad:
def ok_age (age):
    while not (age.isnumeric() and int(age) >= 1):
        age = input("""
    Ingrese una edad válida: """)
    return age

#Función para validar el tiempo máximo:
def ok_max_time (max_time):
    while not (max_time.isnumeric() and int(max_time) > 0):
        max_time = input("Ingrese un tiempo máximo válido (en minutos): ")
    return int(max_time)

#Función para validar el número de vidas:
def ok_lifes (lifes):
    while not (lifes.isnumeric() and int(lifes) > 0):
        lifes = input("""
    Ingresa un número de vidas válido: """)
    return int(lifes)

#Función para validar el número de pistas:
def ok_clues (clues):
    while not (clues.isnumeric() and int(clues) >= 0):
        clues = input("""
    Ingresa un número de pistas válido: """)
    return int(clues)

#Función para el Inicio de Sesión:
def login ():
    user_name = input("""
    Ingrese su nombre de Usuario: """)
    if check_user_name(user_name):
        password = input("""
    Ingrese su Contraseña: """)
        if check_password (user_name, password):
            return user_name, True
        else: 
            print ("""
    Contraseña Inválida.""")
            return user_name, False
    else:
        print("""
    Nombre de Usuario no registrado.""")
        return user_name, False

#Funcioón para Registrarse:
def register ():
    user_name = input("""
    Ingrese su nuevo nombre de Usuario: """)
    user_name = ok_user_name(user_name)  
    password = input("""
    Ingrese su nueva Contraseña: """)
    password = ok_password(password)
    avatar_selection = input("""
    1. Scharifker
    2. Eugenio Mendoza
    3. Pelusa
    4. Gandhi
    Seleccione su avatar (1, 2, 3 o 4): """)
    while True:
        if avatar_selection == "1":
            avatar = "Scharifker"
            break
        elif avatar_selection == "2":
            avatar = "Eugenio Mendoza"
            break
        elif avatar_selection == "3":
            avatar = "Pelusa"
            break
        elif avatar_selection == "4":
            avatar = "Gandhi"
            break
        else:
            avatar_selection = input("""
    Ingrese una opción válida: """)
    age = input("""
    Ingrese su edad: """)
    age = ok_age(age)
    #Llamamiento a la clase que registra a los usuarios en el archivo .txt
    New_Users(user_name, password, avatar, age)
    return True

#Función que da inicio al juego:
def game_begin (difficulty, log_user_name):
    import time
    if difficulty == "1":
        difficulty = "Fácil"
        max_time = 18
        lifes = 5
        clues = 5
    elif difficulty == "2":
        difficulty = "Medio"
        max_time = 12
        lifes = 3
        clues = 3
    elif difficulty == "3":
        difficulty = "Dificil"
        max_time = 7
        lifes = 1
        clues = 2
    elif difficulty == "4":
        difficulty = "Sandbox"
        max_time = (input("Ingrese la cantidad de tiempo máxima deseada (en minutos): "))
        max_time = ok_max_time(max_time)
        lifes = (input("Ingrese la cantidad de vidas deseadas: "))
        lifes = ok_lifes(lifes)
        clues = (input("Ingrese la cantidad de pistas deseadas: "))
        clues = ok_clues(clues)
    begin = input (f"""
    Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), 
    lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto 
    de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. 
    Necesitamos que nos ayudes a recuperar el disco, para eso tienes {max_time} minutos, 
    antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto?
    (Si o No): """).lower()
    while True:
        if begin == "si":
            #Empieza a contar el tiempo.
            tic = time.perf_counter()
            inventory = ["Ninguno"] 
            print("""
    Bienvenido, gracias por tu disposición a ayudarnos a resolver este inconveniente,  
    te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué acciones 
    puedes realizar. Recuerda que el tiempo corre más rápido que un trimestre en este reto.""")
            #Llamamiento a la clase de Rooms para ir a la Biblioteca.
            Rooms(log_user_name, lifes, clues, inventory, tic, difficulty)
            break
        if begin == "no":
            print("""
    Gracias de igual manera, será para la próxima vez, si es que la hay...""")
            exit()
        else: 
            begin = input("""
    Ingresa una opción válida (si o no): """)

#Función para ver las estadísticas:
def statistics():
    while True:
        option = input("""
    Selecciona el tipo de estadística que deseas ver: 
    1. Leaderboard.
    2. Ver cantidad de veces jugadas por Usuario.
    3. Regresar.
    """)
        if option == "1":
            print("""
    -------Leaderboard-------""")
            top = 0
            i = 0
            times = []
            top_5 = []
            top_players = []
            with open ("Games_Played.txt", "r") as statistics:
                all_statistics = statistics.readlines()
            for statistics_info in all_statistics:
                info = statistics_info.split(":")
                times.append(float(info[0]))
            times = sorted(times)
            #Definir los 5 mejores tiempos.
            top_5.append(times[0])
            top_5.append(times[1])
            top_5.append(times[2])
            top_5.append(times[3])
            top_5.append(times[4])
            while True:
                try:
                    for statistics_info in all_statistics:
                        info = statistics_info[:-1].split(":")
                        if top_5[i] == float(info[0]):
                            top_players.append(info)
                            i += 1
                except:
                    break
            for best_players in top_players:
                print(f"""
    ----------Top {top+1}----------
    Nombre: {best_players[3]}
    Avatar: {best_players[4]}
    Tiempo: {best_players[0]}
    Dificultad: {best_players[1]}
    Éxito: {best_players[2]}
    -------------------------""")
                top += 1
        elif option == "2":
            top_counter = 0
            list_of_times = []
            user_names = []
            with open ("Games_Played.txt", "r") as users_database:
                users_info = users_database.readlines()
            #Nombre de los jugadores que han jugado.
            for users_and_passwords in users_info:
                user_and_password = users_and_passwords[:-1].split(":")
                user_names.append(user_and_password[3])
            names = list(set(user_names))
            #Contador de veces jugadas.
            for name in names:
                times = user_names.count(name)
                list_of_times.append(times)
            times_names = dict(zip(names, list_of_times))
            for users, number in sorted(times_names.items(), key=operator.itemgetter(1)):
                print(f"""
    ------------Top {top_counter + 1}-------------
    Jugador: {users}
    Veces jugadas: {number} 
    ------------------------------""")
                top_counter += 1
        elif option == "3":
            break
        else:
            print("""
    Ingresa una opción válida.""")

