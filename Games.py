import Gamesimages
import fractions
import sympy
import random
import requests
response = requests.get("https://api-escapamet.vercel.app/")
response_json = response.json()

#Clase que contiene a todos lo juegos.
class Games ():
    def __init__(self, lifes, clues, inventory, tic):
        self.lifes = lifes
        self.clues = clues
        self.inventory = inventory
        self.tic = tic
    #Juego 1 de la Plaza del Rectorado
    def juego_saman (self):
        name = response_json[2]["objects"][0]["game"]["name"]
        message_requirement = response_json[2]["objects"][0]["game"]["message_requirement"]
        requirement = response_json[2]["objects"][0]["game"]["requirement"]
        award = response_json[2]["objects"][0]["game"]["award"]
        rules = response_json[2]["objects"][0]["game"]["rules"]
        question = response_json[2]["objects"][0]["game"]["questions"]
        if requirement == False:
            requirement = "Ninguno"
        #Solo lo puedes jugar si no tienes la recompensa en tu inventario.
        if award not in self.inventory:
            self.lifes = self.lifes - 1
            print(f"""
    Para acceder a la recompensa de este juego ({award}) deberas superar este desafio:
    {name}
    {message_requirement}
    Items necesarios para jugar: {requirement[0]} y {requirement[1]}
    Reglas: {rules}
    Pregunta:
    {question[random.randint(0,1)]}
    Tienes {self.lifes} vidas.""")
            #Solo lo puedes jugar si tienes los requerimientos en tu inventario.
            if "título Universitario" in self.inventory and "Mensaje: Si estas gradudado puedes pisar el Samán" in self.inventory :
                answer = input("""
    Ingresa la respuesta del desafio: """)
                while True:
                    if answer == "67":
                        print("""
    Respuesta correcta, la recompensa ha sido añadida a tu inventario.""")
                        break
                    elif answer == "41":
                        print("""
    Respuesta correcta, la recompensa ha sido añadida a tu inventario.""")
                        break
                    else:
                        print("""
    Respuesta incorrecta, acabas de perder una vida.""")
                        self.lifes = self.lifes - 1
                        break
            else:
                print(f"""
    No cumples con los requerimientos para realizar este desafio ({requirement}).""")
        else:
            print(f"""
    Ya posees la recompensa de este juego ({award}).""")
    #Juego 2 de la Plaza del Rectorado.
    def juego_banco1 (self):
        name = response_json[2]["objects"][1]["game"]["name"]
        requirement = response_json[2]["objects"][1]["game"]["requirement"]
        award = response_json[2]["objects"][1]["game"]["award"]
        rules = response_json[2]["objects"][1]["game"]["rules"]
        question = response_json[2]["objects"][1]["game"]["questions"][random.randint(0,2)]
        if requirement == False:
            requirement = "Ninguno"
        #Solo lo puedes jugar si no tienes la recompensa en tu inventario.
        if award not in self.inventory:
            print(f"""
    Para acceder a la recompensa de este juego ({award}) deberas superar este desafio:
    {name}
    Items necesarios para jugar: {requirement}
    Reglas: {rules}
    Pregunta: {question["question"]}
    1. {question["answer_2"]}
    2. {question["answer_3"]}
    3. {question["correct_answer"]}
    4. {question["answer_4"]}
    0. Revela una pista.
    
    Tienes {self.lifes} vidas y {self.clues} pistas.""")
            #Solo lo puedes jugar si tienes los requerimientos en tu inventario.
            if requirement in self.inventory:
                answer = input("""
    Ingresa la respuesta del desafio: """)
                while True:
                    if answer == "3":
                        print("""
    Respuesta correcta, la recompensa se añadió a tu inventario.""")
                        self.inventory.append(award)
                        break
                    elif answer == "0" and self.clues > 0:
                            print(f"""
    Pista: {question["clue_1"]}""")
                            self.clues = self.clues - 1
                            answer = input("""
    Ingrese la respuesta del desafio: """)
                    elif answer == "0" and self.clues <= 0:
                        answer = input("""
    No te quedan mas pistas, Ingresa la respuesta del desafio: """)
                    else:
                        print("""
    Respuesta incorrecta, acabas de perder una vida.""")
                        self.lifes = self.lifes - 1
                        break
            else:
                print(f"""
    No cumples con los requerimientos para realizar este desafio ({requirement}).""")
        else:
            print(f"""
    Ya posees la recompensa de este juego ({award}).""")
    #Juego 3 de la Plaza del rectorado.
    def juego_banco2 (self):
        name = response_json[2]["objects"][2]["game"]["name"]
        requirement = response_json[2]["objects"][2]["game"]["requirement"]
        award = response_json[2]["objects"][2]["game"]["award"]
        rules = response_json[2]["objects"][2]["game"]["rules"]
        if requirement == False:
            requirement = "Ninguno"
        #Solo lo puedes jugar si no tienes la recompensa en tu inventario.
        if award not in self.inventory:
            print(f"""
    Para acceder a la recompensa de este juego ({award}) deberas superar este desafio:
    {name}
    Items necesarios para jugar: {requirement}
    Reglas: {rules}
    Pregunta:
    1  2  3  4
    5  6  7  8
    9  10 11 12
    13 14 15 16
    Escribe "0" para recibir una pista.""")
            #Solo lo puedes jugar si tienes los requerimientos en tu inventario.
            if requirement in self.inventory:
                while True:
                    answer1 = input("""
    Selecciona una posición para mostrar el Emoji: """)
                    if answer1 == "1" or answer1 == "16":
                        print("""
    Emoji correspondiente: 😀""")
                    elif answer1 == "2" or answer1 == "15":
                        print("""
    Emoji correspondiente: 🙄""")
                    elif answer1 == "3" or answer1 == "5":
                        print("""
    Emoji correspondiente: 🤮""")
                    elif answer1 == "4" or answer1 == "11":
                        print("""
    Emoji correspondiente: 🥰""")
                    elif answer1 == "6" or answer1 == "9":
                        print("""
    Emoji correspondiente: 😨""")
                    elif answer1 == "7" or answer1 == "10":
                        print("""
    Emoji correspondiente: 🤓""")
                    elif answer1 == "8" or answer1 == "12":
                        print("""
    Emoji correspondiente: 😷""")
                    elif answer1 == "13" or answer1 == "14":
                        print("""
    Emoji correspondiente: 🤑""")
                    answer2 = input("""
    Selecciona una segunda posición para mostrar el Emoji: """)
                    if answer2 == "1" or answer2 == "16":
                        print("""
    Emoji correspondiente: 😀""")
                    elif answer2 == "2" or answer2 == "15":
                        print("""
    Emoji correspondiente: 🙄""")
                    elif answer2 == "3" or answer2 == "5":
                        print("""
    Emoji correspondiente: 🤮""")
                    elif answer2 == "4" or answer2 == "11":
                        print("""
    Emoji correspondiente: 🥰""")
                    elif answer2 == "6" or answer2 == "9":
                        print("""
    Emoji correspondiente: 😨""")
                    elif answer2 == "7" or answer2 == "10":
                        print("""
    Emoji correspondiente: 🤓""")
                    elif answer2 == "8" or answer2 == "12":
                        print("""
    Emoji correspondiente: 😷""")
                    elif answer2 == "13" or answer2 == "14":
                        print("""
    Emoji correspondiente: 🤑""")
                    if ((answer1 == "1" and answer2 == "16") or (answer1 == "16" and answer2 == "1")) or ((answer1 == "2" and answer2 == "15")or(answer1 == "15" and answer2 == "2")) or ((answer1 == "3" and answer2 == "5") or (answer1 == "5" and answer2 == "3")) or ((answer1 == "4" and answer2 == "11") or (answer1 == "11" and answer2 == "4")) or ((answer1 == "6" and answer2 == "9") or (answer1 == "9" and answer2 == "6")) or ((answer1 == "7" and answer2 == "10") or (answer1 == "10" and answer2 == "7")) or ((answer1 == "8" and answer2 == "12") or (answer1 == "12" and answer2 == "8")) or ((answer1 == "13" and answer2 == "14") or (answer1 == "14" and answer2 == "13")):
                        print("""
    Lograste completar el desafio de la memoria, la recompensa ha sido añadida a tu inventario.""")
                        self.inventory.append(award)
                        break
                    elif answer1 == "0" and answer2 == "0":
                        if self.clues > 0:
                            print("""
    Pista: Los emojis en las posiciones 13 y 14 son iguales.""")
                            self.clues = self.clues - 1
                        else:
                            print("""
    No te quedan mas pistas disponibles.""")
                    else:
                        print("""
    Las posiciones seleccionadas no conforman una pareja, intentalo de nuevo.""")
                        self.lifes = self.lifes - 0.25
            else: 
                print(f"""
    No cumples con los requerimientos para realizar este desafio ({requirement}).""")
        else:
            print(f"""
    Ya posees la recompensa de este juego ({award}).""")
    #Juego 1 de la Biblioteca
    def juego_mueble_de_libros(self):
        name = response_json[1]["objects"][0]["game"]["name"]
        requirement = response_json[1]["objects"][0]["game"]["requirement"]
        award = response_json[1]["objects"][0]["game"]["award"]
        rules = response_json[1]["objects"][0]["game"]["rules"]
        question = response_json[1]["objects"][0]["game"]["questions"][random.randint(0,2)]
        word = question["answer"].lower()
        letters = []
        secret = []
        bad_counter = 0
        for letter in word:
            letters.append(letter)
            secret.append("_")
        clue_number = 0
        if requirement == False:
            requirement = "Ninguno"
        #Solo lo puedes jugar si no tienes la recompensa en tu inventario.
        if award not in self.inventory:
            print(f"""
    Para acceder a la recompensa de este juego ({award}) deberas superar este desafio:
    {name}
    Items necesarios para jugar: {requirement}
    Reglas: {rules}
    Enunciado: {question["question"]}
    Palabra secreta: {secret} ({len(secret)} letras) 
    Escribe "0" para recibir una pista (máximo 3).
    {Gamesimages.ahorcados}
    """) 
            #Solo lo puedes jugar si tienes los requerimientos en tu inventario.
            if requirement in self.inventory:
                while True:
                    if bad_counter < 8:
                        if "_" in secret:
                            letter_choice = input("""
    Ingrese una letra: """)
                            if letter_choice.lower() in letters:
                                print("""
    Felicidades, la letra forma parte de la palabra secreta.""")
                                for index,letter in enumerate(letters):
                                    if letter_choice == letter:
                                        secret[index] = letter_choice
                                print(f"""
    {secret}""")
                            elif letter_choice == "0":
                                if self.clues > 0:
                                    if clue_number == 0:
                                        clue = question["clue_1"]
                                        clue_number += 1
                                        self.clues = self.clues - 1
                                    elif clue_number == 1:
                                        clue = question["clue_2"]
                                        clue_number += 1
                                        self.clues = self.clues - 1
                                    elif clue_number == 2:
                                        clue = question["clue_3"]
                                        clue_number += 1
                                        self.clues = self.clues - 1
                                    else:
                                        clue = "No hay mas pistas."
                                    print (f"""
    Pista: {clue}""")
                            elif letter_choice.lower() in "abcdefghijklmnñopqrstuvwxyz":
                                bad_counter += 1
                                print(f"""
    La letra ingresada no forma parte de la palabra secreta, intentalo de nuevo. Te quedan {8 - bad_counter} intentos""")
                                self.lifes = self.lifes - 0.25
                            else:
                                print("""
    Ingresa una letra válida, no es necesario colocar acentos.""")
                        else:
                            print("""
    Felicidades, adivinaste la palabra secreta, la recompensa ha sido añadida a tu inventario.""")
                            self.inventory.append(award)
                            break
                    else:
                        print("""
    Acabas de superar tu limite máximo de intentos y perdiste el desafio.""")
                        break
            else:
                print(f"""
    No cumples con los requerimientos para realizar este desafio ({requirement}).""")
        else:
            print(f"""
    Ya posees la recompensa de este juego ({award}).""")
    #Juego 2 de la Biblioteca.
    def juego_mueble_de_sentarse (self):
        name = response_json[1]["objects"][1]["game"]["name"]
        message_requirement = response_json[1]["objects"][1]["game"]["message_requirement"]
        requirement = response_json[1]["objects"][1]["game"]["requirement"]
        award = response_json[1]["objects"][1]["game"]["award"]
        rules = response_json[1]["objects"][1]["game"]["rules"]
        question = response_json[1]["objects"][1]["game"]["questions"][random.randint(0,2)]
        x = sympy.Symbol("x")
        if requirement == False:
            requirement = "Ninguno"
        #Solo lo puedes jugar si no tienes la recompensa en tu inventario.
        if "Vida Extra 1" not in self.inventory:
            print(f"""
    Para acceder a la recompensa de este juego ({award}) deberas superar este desafio:
    {name}
    {message_requirement}
    Items necesarios para jugar: {requirement}
    Reglas: {rules}
    Enunciado: {question["question"]} 
    Escribe "0" para recibir una pista.""")
            #Solo lo puedes jugar si tienes los requerimientos en tu inventario.
            if requirement in self.inventory:
                answer = input("""
    Ingresa la solución: """)
                while True:
                    if answer == "0":
                        if self.clues > 0:
                            answer = input("""
    Si escribes la palabra "paso" como respuesta, te saltarás la prueba.""")
                            self.clues = self.clues - 1
                        else:
                            answer = input("""
    No te quedan mas pistas disponibles, ingresa la respuesta del desafio: """)
                    if answer == str(sympy.diff(((sympy.sin(x))/2),x).subs(x,sympy.pi)) or answer == str((sympy.diff(((sympy.cos(x))/2 - (sympy.tan(x))/5),x).subs(x,sympy.pi))) or answer == str((sympy.diff(((sympy.sin(x))/5 -(sympy.tan(x))),x).subs(x,sympy.pi))) or answer.lower() == "paso":
                        print("""
    Respuesta correcta, la recompensa se añadió a tu jugador.""")
                        self.lifes = self.lifes + 1
                        self.inventory.append("Vida Extra 1")
                        break
                    else:
                        answer = input("""
    Respuesta incorrecta, intentalo de nuevo: """)
                        self.lifes = self.lifes - 0.25
            else:
                print(f"""
    No cumples con los requerimientos para realizar este desafio ({requirement}).""")
        else:
            print(f"""
    Ya posees la recompensa de este juego ({award}).""")
    #Juego 3 de la Biblioteca.
    def juego_mueble_con_gabetas (self):
        name = response_json[1]["objects"][2]["game"]["name"]
        message_requirement = response_json[1]["objects"][2]["game"]["message_requirement"]
        requirement = response_json[1]["objects"][2]["game"]["requirement"]
        award = response_json[1]["objects"][2]["game"]["award"]
        rules = response_json[1]["objects"][2]["game"]["rules"]
        question = response_json[1]["objects"][2]["game"]["questions"][random.randint(0,2)]
        abc = "abcdefghijklmnñopqrstuvwxyz"
        new_abc = ""
        phrase = question["question"].lower()
        phrase = phrase.replace("á","a")
        number = question["desplazamiento"]
        secret = ""
        for letter in abc:
            if letter in abc:
                letter_position = abc.index(letter)
                new_position = (letter_position + number) % len(abc)
                new_abc += abc[new_position]
        for letter in phrase:
            if letter in abc:
                letter_position = abc.index(letter)
                new_position = (letter_position + number) % len(abc)
                secret += abc[new_position]
            else:
                secret+= letter
        if requirement == False:
            requirement = "Ninguno"
        #Solo lo puedes jugar si no tienes la recompensa en tu inventario.
        if award not in self.inventory:
            print(f"""
    Para acceder a la recompensa de este juego ({award}) deberas superar este desafio:
    {name}
    {message_requirement}
    Items necesarios para jugar: {requirement}
    Reglas: {rules}
    Enunciado: {secret}
    Nuevo Alphabeto: {new_abc} """)
            #Solo lo puedes jugar si tienes los requerimientos en tu inventario.
            if requirement in self.inventory:
                answer = input("""
    Ingresa la respuesta del desafio: """)
                while True:
                    if answer == phrase:
                        print("""
    Respuesta correcta, la recompensa se añadió a tu inventario.""")
                        self.inventory.append(award)
                        break
                    else:
                        answer = input("""
    Respuesta incorrecta, ingresa una nueva respuesta: """)
                        self.lifes = self.lifes - 1
            else:
                print(f"""
    No cumples con los requerimientos para realizar este desafio ({requirement}).""")
        else:
            print(f"""
    Ya posees la recompensa de este juego ({award}).""")
    #Juego de Puertas del Laboratorio.
    def juego_de_puerta_lab (self):
        name = response_json[3]["objects"][0]["game"]["name"]
        message_requirement = response_json[3]["objects"][0]["game"]["message_requirement"]
        requirement = response_json[3]["objects"][0]["game"]["requirement"]
        award = response_json[3]["objects"][0]["game"]["award"]
        rules = response_json[3]["objects"][0]["game"]["rules"]
        question = response_json[3]["objects"][0]["game"]["questions"][random.randint(0,1)]
        if requirement == False:
            requirement = "Ninguno"
        #Solo lo puedes jugar si no tienes la recompensa en tu inventario.
        if "Vida Extra 2" not in self.inventory:
            print(f"""
    Para acceder a la recompensa de este juego ({award}) deberas superar este desafio:
    {name}
    {message_requirement}
    Items necesarios para jugar: {requirement}
    Reglas: {rules}
    Enunciado: {question["question"]}""")
            #Solo lo puedes jugar si tienes los requerimientos en tu inventario.
            if requirement in self.inventory:
                answer = input("""
    Ingresa la respuesta del desafio (true or false): """)
                while True:
                    if answer.lower() == question["answer"].lower():
                        print("""
    Respuesta correcta, la recompensa se añadió a tu inventario.""")
                        self.lifes = self.lifes + 1
                        self.inventory.append("Vida Extra 2")
                        break
                    else:
                        answer = input("""
    Respuesta incorrecta, ingresa una nueva respuesta(true or false): """)
                        self.lifes = self.lifes - 0.5
            else:
                print(f"""
    No cumples con los requerimientos para realizar este desafio ({requirement}).""")
        else:
            print(f"""
    Ya posees la recompensa de este juego ({award}).""")
    #Juego 1 del Laboratorio SL001
    def juego_de_pizarra (self):
        name = response_json[0]["objects"][0]["game"]["name"]
        requirement = response_json[0]["objects"][0]["game"]["requirement"]
        award = response_json[0]["objects"][0]["game"]["award"]
        rules = response_json[0]["objects"][0]["game"]["rules"]
        question = response_json[0]["objects"][0]["game"]["questions"][random.randint(0,2)]
        if question["answer_1"] == "Pilar":
            letter_soup = Gamesimages.letter_soup_1
        elif question["answer_1"] == "Bello":
            letter_soup = Gamesimages.letter_soup_2
        elif question["answer_1"] == "Boada":
            letter_soup = Gamesimages.letter_soup_3
        answer_1 = False
        answer_2 = False
        answer_3 = False
        clue_counter = 0
        if requirement == False:
            requirement = "Ninguno"
        #Solo lo puedes jugar si no tienes la recompensa en tu inventario.
        if "Vida Extra 3" not in self.inventory:
            print(f"""
    Para acceder a la recompensa de este juego ({award}) deberas superar este desafio:
    {name}
    Items necesarios para jugar: {requirement}
    Reglas: {rules}
    Escribe "0" para recibir una pista.
    {letter_soup}""") 
            #Solo lo puedes jugar si tienes los requerimientos en tu inventario.
            if requirement in self.inventory:
                while True:
                    if answer_1 != True or answer_2 != True or answer_3 != True:
                        answer = input("""
    Ingresa una palabra: """)
                        if answer.lower() == question["answer_1"].lower():
                            answer_1 = True
                            print("""
    Palabra correcta""")
                        elif answer.lower() == question["answer_2"].lower():
                            answer_2 = True
                            print("""
    Palabra correcta""")
                        elif answer.lower() == question["answer_3"].lower():
                            answer_3 = True
                            print("""
    Palabra correcta""")
                        elif answer == "0":
                            if self.clues > 0 and clue_counter == 0:
                                print(f"""
    Pistas: 
    {question["clue_1"]}
    {question["clue_2"]}
    {question["clue_3"]}
    No hay mas pistas.""")
                                self.clues = self.clues - 1
                                clue_counter = 1
                            else:
                                print("""
    No te quedan mas pistas disponibles. """)
                        else: 
                            print(""" 
    Palabra incorrecta""")
                            self.lifes = self.lifes - 0.5
                    else:
                        print(""" 
    Encontraste todas las palabras, la recompensa se añadió a tu jugador.""")
                        self.lifes = self.lifes + 1
                        self.inventory.append("Vida Extra 3")
                        break
            else:
                print(f"""
    No cumples con los requerimientos para realizar este desafio ({requirement}).""")
        else:
            print(f"""
    Ya posees la recompensa de este juego ({award}).""")
    #Juego 2 del Laboratorio SL001.
    def juego_de_computadora1 (self):
        name = response_json[0]["objects"][1]["game"]["name"]
        message_requirement = response_json[0]["objects"][1]["game"]["message_requirement"]
        requirement = response_json[0]["objects"][1]["game"]["requirement"]
        award = response_json[0]["objects"][1]["game"]["award"]
        rules = response_json[0]["objects"][1]["game"]["rules"]
        question = response_json[0]["objects"][1]["game"]["questions"][0]
        clue_number = 0
        if requirement == False:
            requirement = "Ninguno"
        #Solo lo puedes jugar si no tienes la recompensa en tu inventario.
        if award not in self.inventory:
            print(f"""
    Para acceder a la recompensa de este juego ({award}) deberas superar este desafio:
    {name}
    {message_requirement}
    Items necesarios para jugar: {requirement}
    Reglas: {rules}
    Enunciado: {question["question"]}
    Escribe "0" para recibir una pista.""")
            #Solo lo puedes jugar si tienes los requerimientos en tu inventario.
            if requirement in self.inventory:
                while True:
                    answer = input("""
    Ingresa la respuesta del desafio: """)
                    try: 
                        if eval(answer) == (int(float((((((question["question"]).split('"'))[1]).replace(",",".")).split(" "))[-2]))):
                            print(f"""
    Respuesta correcta, la recompensa se añadió a tu inventario.""")
                            self.inventory.append(award)
                            break
                        elif answer == "0":
                            if self.clues > 0:
                                if clue_number == 0:
                                    clue = question["clue_1"]
                                    clue_number += 1
                                    self.clues = self.clues - 1
                                elif clue_number == 1:
                                    try:
                                        clue = question["clue_2"]
                                        clue_number += 1
                                        self.clues = self.clues - 1
                                    except:
                                        clue = "No hay mas pistas."
                                elif clue_number == 2:
                                    try:
                                        clue = question["clue_3"]
                                        clue_number += 1
                                        self.clues = self.clues - 1
                                    except:
                                        clue = "No hay mas pistas."
                                else:
                                    clue = "No hay mas pistas."
                                print (f"""
    {clue}""")          
                            else:
                                print("""
    No te quedan mas pistas disponibles.""")
                        else:
                            print("""
    Respuesta incorrecta, vuelve a intentarlo.""")
                        self.lifes = self.lifes - 0.5
                    except:
                        print("""
    Respuesta inválida, intentalo de nuevo.""")
            else:
                print(f"""
    No cumples con los requerimientos para realizar este desafio ({requirement}).""")
        else:
            print(f"""
    Ya posees la recompensa de este juego ({award}).""")
    #Juego 3 del Laboratorio SL001:
    def juego_de_computadora2 (self):
        name = response_json[0]["objects"][2]["game"]["name"]
        message_requirement = response_json[0]["objects"][2]["game"]["message_requirement"]
        requirement = response_json[0]["objects"][2]["game"]["requirement"]
        award = response_json[0]["objects"][2]["game"]["award"]
        rules = response_json[0]["objects"][2]["game"]["rules"]
        question = response_json[0]["objects"][2]["game"]["questions"][random.randint(0,1)]
        clue_number = 0
        if requirement == False:
            requirement = "Ninguno"
        #Solo lo puedes jugar si no tienes la recompensa en tu inventario.
        if award not in self.inventory:
            print(f"""
    Para acceder a la recompensa de este juego ({award}) deberas superar este desafio:
    {name}
    {message_requirement}
    Items necesarios para jugar: {requirement}
    Reglas: {rules}
    Enunciado: {question["question"]}
    Escribe "0" para recibir una pista.""")
            #Solo lo puedes jugar si sabes la contraseña.
            password = input("""
    Ingrese la contraseña de la computadora: """)
            if password == "#ProyectoImposible":
                print("""
    Contraseña correcta.""")
                while True:
                    answer = input("""
    Ingresa la respuesta del desafio: """)
                    if answer in question["answers"]:
                        print(f"""
    Respuesta correcta, la recompensa se añadió a tu inventario.""")
                        self.inventory.append(award)
                        break
                    elif answer == "0":
                        if self.clues > 0:
                            if clue_number == 0:
                                clue = question["clue_1"]
                                clue_number += 1
                                self.clues = self.clues - 1
                            elif clue_number == 1:
                                clue = question["clue_2"]
                                clue_number += 1
                                self.clues = self.clues - 1
                            elif clue_number == 2:
                                clue = question["clue_3"]
                                clue_number += 1
                                self.clues = self.clues - 1
                            else:
                                clue = "No hay mas pistas."
                            print (f"""
    {clue}""")
                        else:
                            print("""
    No te quedan mas pistas disponibles. """)
                    else:
                        print("""
    Respuesta incorrecta, intentalo de nuevo. """)
                        self.lifes = self.lifes - 0.5
            else:
                print(f"""
    Contraseña incorrecta.""")
        else:
            print(f"""
    Ya posees la recompensa de este juego ({award}).""")
    #Juego 1 del Cuarto de Servidores.
    def juego_de_puerta (self):
        name = response_json[-1]["objects"][0]["game"]["name"]
        message_requirement = response_json[-1]["objects"][0]["game"]["message_requirement"]
        requirement = response_json[-1]["objects"][0]["game"]["requirement"]
        award = response_json[-1]["objects"][0]["game"]["award"]
        rules = response_json[-1]["objects"][0]["game"]["rules"]
        abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
        random_letter = abc[random.randint(0,26)]
        question = "Stop: debes responder las siguientes preguntas con palabras que empiecen con la letra: " + random_letter
        if requirement == False:
            requirement = "Ninguno"
        #Solo lo puedes jugar si no tienes la recompensa en tu inventario.
        print(f"""
    Para acceder a la recompensa de este juego ({award}) deberas superar este desafio:
    {name}
    {message_requirement}
    Items necesarios para jugar: {requirement}
    Reglas: {rules}
    Enunciado: {question}""")
        if "carnet" in self.inventory and "Disco Duro" in self.inventory:
            while True:
                answer_country = input("""
    Ingresa un país que empiece con la letra seleccionada: """)
                if answer_country[0].lower() == random_letter:
                    break
                else:
                    answer_country = input("""
    Ingresa un país válido: """)
                    self.lifes = self.lifes - 1
            while True:
                answer_food = input("""
    Ingresa una comida que empiece con la letra seleccionada: """)
                if answer_food[0].lower() == random_letter:
                    break
                else:
                    answer_food = input("""
    Ingresa una comida válida: """)
                    self.lifes = self.lifes - 1
            while True:
                answer_color = input("""
    Ingresa un color que empiece con la letra seleccionada: """)
                if answer_color[0].lower() == random_letter:
                    break
                else:
                    answer_color = input("""
    Ingresa un color válido: """)
                    self.lifes = self.lifes - 1
                print(f"""
    Respuestas correctas.""")
                return True
            else:
                return False
        else:
            print(f"""
    No cumples con los requerimientos para realizar este desafio ({requirement}).""")
    #Juego 2 del Cuarto de Servidores.
    def juego_de_rack (self):
        name = response_json[4]["objects"][1]["game"]["name"]
        requirement = response_json[4]["objects"][1]["game"]["requirement"]
        award = response_json[4]["objects"][1]["game"]["award"] + ": #ProyectoImposible"
        rules = response_json[4]["objects"][1]["game"]["rules"]
        question = response_json[4]["objects"][1]["game"]["questions"][random.randint(0,2)]
        correct_words = []
        mixed_words = []
        for word in question["words"]:
            size= len(word)
            mix = random.sample(word, size)
            mixed_word = ''.join(mix)
            mixed_words.append(mixed_word)
        if requirement == False:
            requirement = "Ninguno"
        #Solo lo puedes jugar si no tienes la recompensa en tu inventario.
        if award not in self.inventory:
            print(f"""
    Para acceder a la recompensa de este juego ({award}) deberas superar este desafio:
    {name}
    Items necesarios para jugar: {requirement}
    Reglas: {rules}
    Enunciado: {question["question"]}. No debes alterar el orden de las palabras en la lista.
    Categoria: {question["category"]}
    Palabras desordenadas: {mixed_words}""")
            #Solo lo puedes jugar si tienes los requerimientos en tu inventario.
            if requirement in self.inventory:
                while True:
                    if correct_words == question["words"]:
                        print("""
    Lograste completar el desafio, la recompensa fue añadida a tu inventario.""")
                        self.inventory.append(award)
                        break
                    elif len(correct_words) > 4:
                        print("""
    Exediste la cantidad maxima de palabras correctas, probablemente hubo un error, intentalo de nuevo.""")
                        break
                    elif correct_words != question["words"]:
                        answer = input("""
    Ingresa una palabra ordenada: """)
                        if answer in question["words"]:
                            print("""
    Palabra correcta. """)
                            correct_words.append(answer)
                        else:
                            print("""
    Palabra incorrecta. """)
                            self.lifes = self.lifes - 0.5
            else:
                print(f"""
    No cumples con los requerimientos para realizar este desafio ({requirement}).""")
        else:
            print(f"""
    Ya posees la recompensa de este juego ({award}).""")
    #Juego 3 del Cuarto de Servidores.
    def juego_de_papelera (self):
        name = response_json[-1]["objects"][2]["game"]["name"]
        requirement = response_json[-1]["objects"][2]["game"]["requirement"]
        award = response_json[-1]["objects"][2]["game"]["award"]
        rules = response_json[-1]["objects"][2]["game"]["rules"]
        question = response_json[-1]["objects"][2]["game"]["questions"]
        number = random.randint(1,15)
        wrong_counter = 0
        if requirement == False:
            requirement = "Ninguno"
        #Solo lo puedes jugar si no tienes la recompensa en tu inventario.
        if award not in self.inventory:
            print(f"""
    Para acceder a la recompensa de este juego ({award}) deberas superar este desafio:
    {name}
    Items necesarios para jugar: {requirement}
    Reglas: {rules}
    Enunciado: {question[0]["question"]}
    Escribe "0" para recibir una pista.""") 
            #Solo lo puedes jugar si tienes los requerimientos en tu inventario.
            if requirement in self.inventory:   
                while True:
                    if wrong_counter == 3:
                        self.lifes = self.lifes - 0.25
                        wrong_counter = 0
                    answer = input("""
    Ingresa un numero del 1 al 15: """)
                    if answer == str(number):
                        print("""
    Acertaste el número y la recompensa ha sido añadida a tu inventario. """)
                        self.inventory.append(award)
                        break
                    elif answer == "0":
                        if self.clues > 0:
                            answer = input("""
    Ingresa un numero del 1 al 15 para revelar la pista: """)
                            while not answer.isnumeric():
                                answer = input("""
    Ingresa un número válido: """)
                            if int(answer) < number and number - int(answer) > 3:
                                clue = "Estas muy por debajo de la respuesta."
                                self.clues = self.clues - 1
                            elif int(answer) < number and number - int(answer) <= 3:
                                clue = "Estas poco por debajo de la respuesta."
                                self.clues = self.clues - 1
                            elif int(answer) > number and int(answer) - number > 3:
                                clue = "Estas muy por encima de la respuesta."
                                self.clues = self.clues - 1
                            elif int(answer) > number and int(answer) - number <= 3:
                                clue = "Estas poco por encima de la respuesta."
                                self.clues = self.clues - 1
                            else:
                                clue = "Hubo un error al generar la pista, intentalo de nuevo."
                            print (f"""
    {clue}""")
                        else:
                            print("""
    No te quedan mas pistas disponibles. """)
                    else:
                        print("""
    Respuesta incorrecta. """)
                        wrong_counter += 1
            else:
                print(f"""
    No cumples con los requerimientos para realizar este desafio ({requirement}).""")
        else:
            print(f"""
    Ya posees la recompensa de este juego ({award}).""")