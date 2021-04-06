#Función principal de todo el proyecto.
def main ():
    import functions
    #Mensaje de Bienvenida.
    print("""
    Bienvenido a mi proyecto de Algoritmos y Programación. Para este trimestre
    correspondia realizar un Scape Room y podría decirse que lo he logrado.
    Espero que lo disfrutes.""")
    #Iniciar sesion o Registrarse.
    login_or_register = input("""
    Seleccione una opción (1, 2, 3 o 4):
    1. Iniciar Sesión.
    2. Registrarse.
    3. Estadísticas.
    4. Salir.
    """)
    while True:
    #Opción 1, Iniciar Sesion:
        if login_or_register == "1":
            log_user_name, check = functions.login()
            if check == True:
                print(f"""
    Usuario: {log_user_name.user_name} su sesión ha sido iniciada correctamente.""")
    #Una vez iniciada sesion correctamente, se imprimen las instrucciones y se selecciona la dificultad:
                print("""
    Instrucciones para jugar:
    Una vez empiece el juego se te presentarán una serie de opciones enlistadas,
    lo único que debes hacer es ingresar el número de la opción que deseas seleccionar.
    Casi todas las habitaciones estan conformadas por 3 desafios que deberás superar
    para asi recolectar los instrumentos para desbloquear nuevas salas y nuevos desafios.
    Las instrucciones de cada desafio estarán escritas al principio de los mismos, 
    asi que recuerda leer todo con atención.
    Te deseo mucha suerte y espero que te diviertas.""")
                difficulty = input("""
    Seleccione una dificultad (1, 2, o 4):
    1. Facil. (5 vidas, 5 pistas y 15 minutos)
    2. Medio. (3 vidas, 3 pistas y 10 minutos)
    3. Dificil. (1 vida, 2 pistas y 5 minutos)
    4. Sandbox. (Tú seleccionas el tiempo, las vidas y las pistas deseadas para jugar.)
    """)        
                #Llamamiento a la función que da inicio al juego
                functions.game_begin(difficulty, log_user_name)
            else: 
                login_or_register = input("""
    Seleccione una opción (1, 2, 3 o 4):
    1. Iniciar Sesión.
    2. Registrarse.
    3. Estadísticas.
    4. Salir.
    """)
    #Opción 2, Registrarse:
        elif login_or_register == "2":
            new_user, check_1 = functions.register()
            if check_1 == True:
                print(f"""
    Usuario "{new_user.user_name}" registrado Correctamente.""")
                login_or_register = input("""
    Seleccione una opción (1, 2, 3 o 4):
    1. Iniciar Sesión.
    2. Registrarse.
    3. Estadísticas.
    4. Salir.
    """)
            else:
                login_or_register = input("""
    Seleccione una opción (1, 2, 3 o 4):
    1. Iniciar Sesión.
    2. Registrarse.
    3. Estadísticas.
    4. Salir.
    """)
    #Opción 3, Estadísticas
        elif login_or_register == "3":
            functions.statistics()
            login_or_register = input("""
    Seleccione una opción (1, 2, 3 o 4):
    1. Iniciar Sesión.
    2. Registrarse.
    3. Estadísticas.
    4. Salir.
    """)
    #Opción 4, Salir
        elif login_or_register == "4":
            break
    #En caso de que la opción no sea válida:
        else:
            login_or_register = input("""
    Ingrese una opción válida: """)

if __name__ == "__main__":
    main()
