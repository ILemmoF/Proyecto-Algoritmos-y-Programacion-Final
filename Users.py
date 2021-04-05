#Clase para registrar nuevos usuarios:
class New_Users ():
    def __init__ (self, user_name, password, avatar, age):
        self.user_name = user_name
        self.password = password
        self.avatar = avatar
        self.age = age
        New_Users.save_user(self)
    def save_user (self):
        with open ("Users_Database.txt", "a+") as users_database:
            users_database.write(f"{self.user_name}:{self.password}:{self.avatar}:{self.age}\n")

#Clase para recopilar la informacion del usuario al momento de logearse:
class Users ():
    def __init__ (self, user_name):
        self.user_name = user_name
        with open ("Users_Database.txt", "r") as users_database:
            users_info = users_database.readlines()
        for users in users_info:
            names = users.split(":")
            if self.user_name == names[0]:
                self.avatar = names [2]
                self.age = names [3]

#Clase para crear las estadisticas al final de cada partida:
class Users_Stats(Users):
    def __init__(self, user_name, difficulty, timer, succes):
        Users.__init__(self, user_name)
        self.difficulty = difficulty
        self.timer = timer 
        self.succes = succes
        Users_Stats.write_stats(self)
    def write_stats (self):
        with open ("Games_Played.txt", "a+") as games_played:
            games_played.write(f"{self.timer}:{self.difficulty}:{self.succes}:{self.user_name}:{self.avatar}:{self.age}")
