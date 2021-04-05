# with open("Users_Database.txt", "a+") as dbe:
#     dbe.write("Hola")
# import random
# import requests
# response = requests.get("https://api-escapamet.vercel.app/")
# response_json = response.json()

# question = response_json[1]["objects"][1]["game"]["questions"][random.randint(0,2)]

# function= (str(question["question"][:-2].split("f(x)=")))

# print(function)
# diccionario = {"name": "Plaza Rectorado",
# "objects": [
# {"name": "Saman",
# "position": "center",
# "game": {
# "name": "Encuentra la lógica y resuelve",
# "message_requirement": "pierdes una vida por pisar el samán 🥵",
# "requirement": ["Titulo Universitario","Mensaje"],
# "award": "Disco Duro",
# "rules": "pierdes una vida por pisar el samán 🥵, pero si tienes en tu inventario lo requerido, puedes jugar el juego del Samán",
# "questions": ["🧡+🧡+🧡=45 \n 🍌+🍌+🧡=23 \n 🍌+⏰+⏰=10 \n ⏰+🍌+🍌x🧡=?",
# "🐧+🐧+🐧=27 \n 🐧+🐝+🐝=19 \n 🐝+🐦+🐦=13 \n 🐝x🐧-🐦=?"]}}]}

# reglas = response_json[2]["objects"][0]["game"]["questions"]
# print(reglas)

# class Prueba():
#     def __init__ (self,x, y):
#         self.x = x
#         self.y = y
#         Prueba.Suma(self)
#     def Suma (self):
#         self.x = self.x * self.y
#         Prueba.Imprimir(self)
#     def Imprimir (self):
#         print (self.x)
#         Prueba.Resta(self)
#     def Resta (self):
#         self.y = self.y - self.x
#         print(self.y)
# Prueba(2,3)

# class Prueba(): 
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#         Prueba.suma(self)
#     def suma(self):
#         self.num3 = self.num1 + self.num2
#         print(self.num3)
#         Prueba.resta(self)
#     def resta(self):
#         self.num4 = self.num1 - self.num2
#         print(self.num4)

# class Prueba2(Prueba):
#     def __init__(self,num1,num2):
#         Prueba.__init__(self, num1, num2)
#         Prueba2.multiplicacion(self)
#     def multiplicacion(self):
#         self.num5 = self.num1 * self.num2
#         print(self.num5)
# Prueba2(5,4)

# import math
# import sympy
# x = sympy.Symbol("x")
# y = ((math.sin(x))/2)
# z = sympy.diff(y,x)
# print(z)
# import fractions
# import math
# import sympy 

# x = sympy.Symbol("x")
# # y = ((cos(x))/2 - (tan(x))/5)
# # print(sympy.diff(y,x))
# sympy.diff(math.cos(math.sin(x**3)),x)


# answer = input("""
# Ingresa una palabra o ingresa 0 para pistas: """)
# while True:
#     if answer_1 != True and answer_2 != True and answer_3 != True:
#         if answer == question["answer_1"]:
#             answer_1 = True
#         elif answer == question["answer_2"]:
#             answer_2 = True
#         elif answer == question["answer_3"]:
#             answer_2 = True
#         elif answer == "0":
#             answer = input(""" Pistas """)
#         else: 
#             answer = input(""" Palabra incorrecta: """)
#     else:
#         print(""" Lo lograste. """)
#         break

# if answer.lower() == question["answer_1"].lower() or answer.lower() == question["answer_2"].lower() or answer.lower() == question["answer_3"].lower():
#                         answer_1 = input("""
#     Palabra correcta, ingresa otra palabra o escribe "0" para unas pistas: """)
#                         if (answer_1.lower() == question["answer_1"].lower() or answer_1.lower() == question["answer_2"].lower() or answer_1.lower() == question["answer_3"].lower()) and answer_1 != answer:
#                             answer_2 = input("""
#     Palabra correcta, ingresa otra palabrao escribe "0" para unas pistas: """)
#                             if answer_2.lower() == question["answer_1"].lower() or answer_2.lower() == question["answer_2"].lower() or answer_2.lower() == question["answer_3"].lower()) and answer_2 != answer and answer_2 != answer_1:
#                                 print("""
#     Palabra correcta, lograste superar el desafio, la recompensa se añadió a tu inventario.""")
#                                 self.inventory.append(award)
#                                 break
#                             elif answer_2 == "0":
#                                 answer_2 = input(f"""
#     Pistas: 
#     {question["clue_1"]}
#     {question["clue_2"]}
#     {question["clue_3"]}
#     No hay mas pistas, ingresa una palabra: """)
#                                 self.clues = self.clues - 1
#                             else: 
#                                 answer_2 = input("""
#     Palabra incorrecta, ingresa otra palabrao escribe "0" para unas pistas: """)
#                         elif answer_1 == "0":
#                             answer_1 = input(f"""
#     Pistas: 
#     {question["clue_1"]}
#     {question["clue_2"]}
#     {question["clue_3"]}
#     No hay mas pistas, ingresa una palabra: """)
#                             self.clues = self.clues - 1
#                         else:
#                             answer_1 = input("""
#     Palabra incorrecta, ingresa otra palabrao escribe "0" para unas pistas: """)
#                     elif answer == "0":
#                             answer = input(f"""
#     Pistas: 
#     {question["clue_1"]}
#     {question["clue_2"]}
#     {question["clue_3"]}
#     No hay mas pistas, ingresa una palabra: """)
#                             self.clues = self.clues - 1
#                     else:
#                         answer = input("""
#     Palabra incorrecta, ingresa otra palabrao escribe "0" para unas pistas: """)

# import random

# tamano = 4
# abecedario = 'vaso'
# desordenar = random.sample(abecedario, tamano)
# palabra = ''.join(desordenar)
# print(palabra)

# lista = [1,2,3,4,8]
# largo = len(lista)
# print (largo)

# ['😀', '🙄', '🤮', '🥰']                                                   
# ['🤮', '😨', '🤓', '😷']                                                  
# ['😨', '🤓', '🥰', '😷']                                                   
# ['🤑', '🤑', '🙄', '😀']
#     1  2  3  4
#     5  6  7  8
#     9  10 11 12
#     13 14 15 16

# # abc = "abcdefghijklmnñopqrstuvwxyz"
# # abc_2 = "cdefghijklmnñopqrstuvwxyzab"
# # abc_4 = "efghijklmnñopqrstuvwxyzabcd"
# # abc_5 = "fghijklmnñopqrstuvwxyzabcde"

# import time

# tic = time.perf_counter()
# prueba = input("Tarda: ")
# toc = time.perf_counter()
# print(toc - tic)

# with open ("Users_Database.txt", "r") as users_database:
#     users_info = users_database.readlines()
# for users in users_info:
#     names = users[:-1].split(":")
#     if user_name == names[0]:
#         avatar = names [2]
#         age = names [3]
# print(avatar)
# x = []
# with open ("Games_Played.txt", "r") as statistics:
#         all_statistics = statistics.readlines()
# for info in all_statistics:
#     idk = info.split(":")
#     x.append(idk)
# print(x)
# print("""
#     -------Leaderboard-------""")
# top = 0
# i = 0
# times = []
# top_5 = []
# top_players = []
# with open ("Games_Played.txt", "r") as statistics:
#     all_statistics = statistics.readlines()
# for statistics_info in all_statistics:
#     info = statistics_info.split(":")
#     times.append(float(info[0]))
# times = sorted(times)
# top_5.append(times[0])
# top_5.append(times[1])
# top_5.append(times[2])
# top_5.append(times[3])
# top_5.append(times[4])
# while True:
#     try:
#         for statistics_info in all_statistics:
#             info = statistics_info[:-1].split(":")
#             if top_5[i] == float(info[0]):
#                 top_players.append(info)
#                 i += 1
#     except:
#         break
# for best_players in top_players:
#     print(f"""
#     ----------Top {top+1}----------
#     Nombre: {best_players[1]}
#     Tiempo: {best_players[0]}
#     Dificultad: {best_players[4]}
#     Éxito: {best_players[5]}
#     -------------------------""")
#     top += 1
# import operator

# top_counter = 0
# list_of_times = []
# user_names = []
# with open ("Games_Played.txt", "r") as users_database:
#     users_info = users_database.readlines()
# for users_and_passwords in users_info:
#     user_and_password = users_and_passwords[:-1].split(":")
#     user_names.append(user_and_password[1])
# names = list(set(user_names))
# for name in names:
#     times = user_names.count(name)
#     list_of_times.append(times)
# print(names)
# print(list_of_times)
# times_names = dict(zip(names, list_of_times))
# print(times_names)
# for users, number in sorted(times_names.items(), key=operator.itemgetter(1)):
#     print(f"""
#     ------------Top {top_counter + 1}-------------
#     Jugador: {users}
#     Veces jugadas: {number} 
#     ------------------------------""")
#     top_counter +=1


# word = "pepino"
# letters = []
# secret = []
# for letter in word:
#     letters.append(letter)
#     secret.append("_")
# while True:
#     if "_" in secret:
#         letter_choice = input("Ingrese una letra: ")
#         if letter_choice in letters:
#             print("Letra correcta.")
#             for index,letter in enumerate(letters):
#                 if letter_choice == letter:
#                     secret[index] = letter_choice
#             print(secret)
#         else:
#             print("Letra incorrecta, intentalo de nuevo.")
#     else:
#         print("Lo lograste")
#         break


# # Obtenemos mensaje a cifrar desde el usuario
# # llamamos a upper para obtener sólo mayúsculas
# texto = input("Mensaje > ").lower()

# # Pedimos al usuario la cantidad de desplazamiento
# n = int(input("Desplazamiento > "))

# # Abecedario a utilizar en el cifrado
# abc = "abcdefghijklmnñopqrstuvwxyz"

# # Variable para guardar mensaje cifrado
# cifrado = ""
# for letter in phrase:
#     # Si la letra está en el abecedario se reemplaza
#     if letter in abc:
#         letter_position = abc.index(letter)
#         # Sumamos para movernos a la derecha del abc
#         new_position = (letter_position + number) % len(abc)
#         secret += abc[new_position]
#     else:
#         # Si no está en el abecedario sólo añadelo
#         secret+= letter

# print("Mensaje cifrado:", cifrado)

# x = "oidutse ne al ortem aireinegni ed sametsis"
# y = x[::-1]
# print (y)
# answer = input("Ingresa: ")
# if eval(answer) == 4:
#     print("Eso")
# else:
#     print("Bolsa")

# def check_password (user_name, password):
#     with open ("Users_Database.txt", "r") as users_database:
#         users_info = users_database.readlines()
#     for users_and_passwords in users_info:
#         user_and_password = users_and_passwords[:-1].split(":")
#         print(user_and_password)


# check_password("NachoTC","Soyelcreador")ç

# frase = "Hola/Mundo"
# hola = ((frase.split("/"))[0])[::-1]
# print(hola)
# import fractions
# import random
# import requests
# response = requests.get("https://api-escapamet.vercel.app/")
# response_json = response.json()
# question = response_json[0]["objects"][1]["game"]["questions"][0]
# question = response_json[1]["objects"][1]["game"]["questions"][1]
# hola = (((question["question"]).split("\\"))[0]).replace(",",".")
# print(hola)

# import sympy
# x = sympy.Symbol("x")

# print(str((sympy.diff(((sympy.cos(x))/2 - (sympy.tan(x))/5),x).subs(x,sympy.pi))))

# import random
# import requests
# response = requests.get("https://api-escapamet.vercel.app/")
# response_json = response.json()

# question = response_json[0]["objects"][1]["game"]["questions"][1]

# print((((question["question"]).split('"'))[-2])[::-1])

#or eval(answer) == ((((question["question"]).split('"'))[-2])[::-1]) or eval(answer) == "estudio en la metro ingenieria de sistemas" or answer == "estudio en la metro ingenieria de sistemas"