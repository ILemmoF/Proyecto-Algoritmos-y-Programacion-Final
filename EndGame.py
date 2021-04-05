from Users import  Users_Stats

#Función que termina el Juego:
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
        succes = "Fracasado"
        print("""
    Lastimosamente no lograste evitar la catástrofe antes de que se te acabara el tiempo.
    Tu tiempo de juego se ha añadido a las estadisticas correctamente.""")
    Users_Stats(log_user_name, difficulty, timer, succes)
    exit()
