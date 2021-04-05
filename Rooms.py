import Roomsimages
from Games import Games
from EndGame import end_game

#Clase donde estan definidos todos los cuartos.
class Rooms ():
    def __init__(self, log_user_name, lifes, clues, inventory, tic, difficulty):
        self.lifes = lifes
        self.clues = clues
        self.inventory = inventory
        self.tic = tic
        self.difficulty = difficulty
        Rooms.biblioteca(self, log_user_name)
    #Plaza del Rectorado
    def plaza_rectorado (self, log_user_name):
        print(f"""
    {Roomsimages.saman}
    Ahora estas en la Plaza del Rectorado.""")
        option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Avanzar al Banco 1 (lado izquierdo de la plaza).
    2. Avanzar el Saman (centro de la plaza).
    3. Avanzar al Banco 2 (lado derecho de la plaza).
    4. Salir de la habitación y dirigirte a la Biblioteca.
    0. Terminar partida.
    """)
        while True:
            if self.lifes >= 0:
                if option == "1":
                    Games(self.lifes, self.clues, self.inventory, self.tic)
                    Games.juego_banco1(self)
                    option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Avanzar al Banco 1 (lado izquierdo de la plaza).
    2. Avanzar el Saman (centro de la plaza).
    3. Avanzar al Banco 2 (lado derecho de la plaza).
    4. Salir de la habitación y dirigirte a la Biblioteca.
    0. Terminar partida.
    """)
                elif option == "2":
                    Games(self.lifes, self.clues, self.inventory, self.tic)
                    Games.juego_saman(self)
                    option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Avanzar al Banco 1 (lado izquierdo de la plaza).
    2. Avanzar el Saman (centro de la plaza).
    3. Avanzar al Banco 2 (lado derecho de la plaza).
    4. Salir de la habitación y dirigirte a la Biblioteca.
    0. Terminar partida.
    """)
                elif option == "3":
                    Games(self.lifes, self.clues, self.inventory, self.tic)
                    Games.juego_banco2(self)
                    option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Avanzar al Banco 1 (lado izquierdo de la plaza).
    2. Avanzar el Saman (centro de la plaza).
    3. Avanzar al Banco 2 (lado derecho de la plaza).
    4. Salir de la habitación y dirigirte a la Biblioteca.
    0. Terminar partida.
    """)
                    option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Avanzar al Banco 1 (lado izquierdo de la plaza).
    2. Avanzar el Saman (centro de la plaza).
    3. Avanzar al Banco 2 (lado derecho de la plaza).
    4. Salir de la habitación y dirigirte a la Biblioteca.
    0. Terminar partida.
    """)
                elif option == "4":
                    Rooms.biblioteca(self, log_user_name)
                elif option == "0":
                    print("""
    Gracias por intentar jugar.""")
                    exit()
                else:
                    option = input("""
    Ingrese una opción válida: """)
            else:
                print("""
    Te quedaste sin vidas y acabas de perder el juego, gracias por intenar jugarlo.""")
                exit()
    #Biblioteca
    def biblioteca (self, log_user_name):
        print(f"""
    {Roomsimages.biblioteca}
    Ahora estas en la Biblioteca.""")
        option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Salir de la habitacion y dirigirte a la Plaza del Rectorado.
    2. Avanzar al Mueble de sentarse (lado izquierdo de la habitación).
    3. Avanzar el Mueble de libros (centro de la habitación).
    4. Avanzar al Mueble con gabetas (lado derecho de la habitación).
    5. Salir de la habitación y dirigirte a la Puerta de los Laboratorios.
    0. Terminar partida.
    """)
        while True: 
            if self.lifes >= 0:
                if option == "1":
                    Rooms.plaza_rectorado(self, log_user_name)
                elif option == "2":
                    Games(self.lifes, self.clues, self.inventory, self.tic)
                    Games.juego_mueble_de_sentarse(self)
                    option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Salir de la habitacion y dirigirte a la Plaza del Rectorado.
    2. Avanzar al Mueble de sentarse (lado izquierdo de la habitación).
    3. Avanzar el Mueble de libros (centro de la habitación).
    4. Avanzar al Mueble con gabetas (lado derecho de la habitación).
    5. Salir de la habitación y dirigirte a la Puerta de los Laboratorios.
    0. Terminar partida.
    """)
                elif option == "3":
                    Games(self.lifes, self.clues, self.inventory, self.tic)
                    Games.juego_mueble_de_libros(self)
                    option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Salir de la habitacion y dirigirte a la Plaza del Rectorado.
    2. Avanzar al Mueble de sentarse (lado izquierdo de la habitación).
    3. Avanzar el Mueble de libros (centro de la habitación).
    4. Avanzar al Mueble con gabetas (lado derecho de la habitación).
    5. Salir de la habitación y dirigirte a la Puerta de los Laboratorios.
    0. Terminar partida.
    """)
                elif option == "4":
                    Games(self.lifes, self.clues, self.inventory, self.tic)
                    Games.juego_mueble_con_gabetas(self)
                    option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Salir de la habitacion y dirigirte a la Plaza del Rectorado.
    2. Avanzar al Mueble de sentarse (lado izquierdo de la habitación).
    3. Avanzar el Mueble de libros (centro de la habitación).
    4. Avanzar al Mueble con gabetas (lado derecho de la habitación).
    5. Salir de la habitación y dirigirte a la Puerta de los Laboratorios.
    0. Terminar partida.
    """)
                elif option == "5":
                    Rooms.puerta_de_laboratorio(self, log_user_name)
                elif option == "0":
                    print("""
    Gracias por intentar jugar.""")
                    exit()
                else:
                    option = input("""
    Ingrese una opción válida: """)
            else:
                print("""
        Te quedaste sin vidas y acabas de perder el juego, gracias por intenar jugarlo.""")
                exit()
    #Puerta del Laboratorio
    def puerta_de_laboratorio (self, log_user_name):
        print(f"""
    {Roomsimages.puerta_de_laboratorio}
    Ahora estas en la Puerta del Laboratorio.""")
        option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Salir de la habitacion y dirigirte a la Biblioteca.
    2. Avanzar a la puerta (centro de la habitación).
    3. Salir de la habitación y dirigirte al Laboratorio SL001.
    0. Terminar partida.
    """)
        while True:
            if self.lifes >= 0:
                if option == "1":
                    Rooms.biblioteca(self, log_user_name)
                elif option == "2":
                    Games(self.lifes, self.clues, self.inventory, self.tic)
                    Games.juego_de_puerta_lab(self)
                    option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Salir de la habitacion y dirigirte a la Biblioteca.
    2. Avanzar hacia a la puerta (centro de la habitación).
    3. Salir de la habitación y dirigirte al Laboratorio SL001.
    0. Terminar partida.
    """)
                elif option == "3" and "libro de Física" in self.inventory:
                    Rooms.laboratorios_SL001(self, log_user_name)
                elif option == "3" and "libro de Física" not in self.inventory:
                    print("""
    No es posible ingresar al Laboratorio Sl001 sin el libro de Física.""")
                    option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Salir de la habitacion y dirigirte a la Biblioteca.
    2. Avanzar hacia a la puerta (centro de la habitación).
    3. Salir de la habitación y dirigirte al Laboratorio SL001.
    0. Terminar partida.
    """)
                elif option == "0":
                    print("""
    Gracias por intentar jugar.""")
                    exit()
                else:
                    option = input("""
    Ingrese una opción válida: """)
            else:
                print("""
    Te quedaste sin vidas y acabas de perder el juego, gracias por intenar jugarlo.""")
                exit()
    #Laboratorio Sl001.
    def laboratorios_SL001 (self, log_user_name):
        print(f"""
    {Roomsimages.laboratorio}
    Ahora estas en los Laboratorios SL001""")
        option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Salir de la habitacion y dirigirte a la Puerta del Laboratorio.
    2. Avanzar hacia la computadora 1 (lado izquierdo de la habitación).
    3. Avanzar hacia la pizarra (centro de la habitación).
    4. Avanzar hacia la computadora 2 (lado derecho de la habitación).
    5. Salir de la habitación y dirigirte al Cuarto de Servidores.
    0. Terminar partida.
    """)
        while True:
            if self.lifes >= 0:
                if option == "1":
                    Rooms.puerta_de_laboratorio(self, log_user_name)
                elif option == "2":
                    Games(self.lifes, self.clues, self.inventory, self.tic)
                    Games.juego_de_computadora1(self)
                    option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Salir de la habitacion y dirigirte a la Puerta del Laboratorio.
    2. Avanzar hacia la computadora 1 (lado izquierdo de la habitación).
    3. Avanzar hacia la pizarra (centro de la habitación).
    4. Avanzar hacia la computadora 2 (lado derecho de la habitación).
    5. Salir de la habitación y dirigirte al Cuarto de Servidores.
    0. Terminar partida.
    """)
                elif option == "3":
                    Games(self.lifes, self.clues, self.inventory, self.tic)
                    Games.juego_de_pizarra(self)
                    option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Salir de la habitacion y dirigirte a la Puerta del Laboratorio.
    2. Avanzar hacia la computadora 1 (lado izquierdo de la habitación).
    3. Avanzar hacia la pizarra (centro de la habitación).
    4. Avanzar hacia la computadora 2 (lado derecho de la habitación).
    5. Salir de la habitación y dirigirte al Cuarto de Servidores.
    0. Terminar partida.
    """)
                elif option == "4":
                    Games(self.lifes, self.clues, self.inventory, self.tic)
                    Games.juego_de_computadora2(self)
                    option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Salir de la habitacion y dirigirte a la Puerta del Laboratorio.
    2. Avanzar hacia la computadora 1 (lado izquierdo de la habitación).
    3. Avanzar hacia la pizarra (centro de la habitación).
    4. Avanzar hacia la computadora 2 (lado derecho de la habitación).
    5. Salir de la habitación y dirigirte al Cuarto de Servidores.
    0. Terminar partida.
    """)
                elif option == "5":
                    Rooms.cuarto_de_servidores(self, log_user_name)
                elif option == "0":
                    print("""
    Gracias por intentar jugar.""")
                    exit()
                else:
                    option = input("""
    Ingrese una opción válida: """)
            else:
                print("""
    Te quedaste sin vidas y acabas de perder el juego, gracias por intenar jugarlo.""")
                exit()
    #Cuarto de Servidores.
    def cuarto_de_servidores(self, log_user_name):
        print(f"""
    {Roomsimages.cuarto_de_servidores}
    Ahora estas en el Cuarto de Servidores.""")
        option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Salir de la habitacion y dirigirte al Laboratorio SL001.
    2. Avanzar al rack (lado izquierdo de la habitación).
    3. Avanzar a la puerta para intentar reparar el servidor (centro de la habitación).
    4. Avanzar a la papelera (lado derecho de la habitación).
    0. Terminar partida.
    """)
        while True:
            if self.lifes >= 0:
                if option == "1":
                    Rooms.laboratorios_SL001(self, log_user_name)
                elif option == "2":
                    Games(self.lifes, self.clues, self.inventory, self.tic)
                    Games.juego_de_rack(self)
                    option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Salir de la habitacion y dirigirte al Laboratorio SL001.
    2. Avanzar al rack (lado izquierdo de la habitación).
    3. Avanzar a la puerta para intentar reparar el servidor (centro de la habitación).
    4. Avanzar a la papelera (lado derecho de la habitación).
    0. Terminar partida.
    """)
                elif option == "3":
                    Games(self.lifes, self.clues, self.inventory, self.tic)
                    #Si la prueba final del proyecto retorna True, indicando que se completó con éxito, el juego se termina llamando a la función end_game.
                    if Games.juego_de_puerta(self):
                        end_game(self.tic, log_user_name, self.difficulty)
                    else:
                    #En caso de que no haya sido completada, el juego seguirá corriendo.
                        option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Salir de la habitacion y dirigirte al Laboratorio SL001.
    2. Avanzar al rack (lado izquierdo de la habitación).
    3. Avanzar a la puerta para intentar reparar el servidor (centro de la habitación).
    4. Avanzar a la papelera (lado derecho de la habitación).
    0. Terminar partida.
    """)
                elif option == "4":
                    Games(self.lifes, self.clues, self.inventory, self.tic)
                    Games.juego_de_papelera(self)
                    option = input(f"""
    Te quedan {self.lifes} vidas y {self.clues} pistas. Inventario: {self.inventory}
    ¿Que deseas hacer?
    1. Salir de la habitacion y dirigirte al Laboratorio SL001.
    2. Avanzar al rack (lado izquierdo de la habitación).
    3. Avanzar a la puerta para intentar reparar el servidor (centro de la habitación).
    4. Avanzar a la papelera (lado derecho de la habitación).
    0. Terminar partida.
    """)
                elif option == "0":
                    print("""
    Gracias por intentar jugar.""")
                    exit()
                else:
                    option = input("""
    Ingrese una opción válida: """)
            else:
                print("""
    Te quedaste sin vidas y acabas de perder el juego, gracias por intenar jugarlo.""")
                exit()

