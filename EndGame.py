from Users import  Users_Stats

#Función que termina el Juego, solo se llega aqui si completa el Scape Room, sin importar si no lo hizo en el tiempo estipulado:
def end_game(tic, log_user_name, difficulty):
    import time
    toc = time.perf_counter()
    if difficulty == "Fácil":
        max_time = 18
    elif difficulty == "Medio":
        max_time = 12
    elif difficulty == "Dificil":
        max_time = 7
    elif difficulty == "Sandbox":
        max_time = 100000000
    timer = (toc - tic) / 60
    if timer < max_time:
        succes = "Completado"
        print("""
    ¡Felicidades! Has logrado evitar una catástrofe en la Unimet.
    Tu tiempo de juego se ha añadido a las estadisticas correctamente.""")
    else:
        #Si completo la partida pero no en el tiempo estipulado,le saldrá "Fracasado" en las estadísticas, pero igual se guarda ya que lo culminó.
        succes = "Fracasado"
        print("""
    Lastimosamente no lograste evitar la catástrofe antes de que se te acabara el tiempo.
    Tu tiempo de juego se ha añadido a las estadisticas correctamente.""")
    #Generador de estadisticas de la partida completada.
    stats = Users_Stats(log_user_name, difficulty, timer, succes)
    #Aquie iba a generar las estadisticas de una manera diferente haciendo el uso del objeto "stats" pero no me daba el tiempo porque se me complicaba el tema de la Herencia.
    exit()
