import random

def jugar():
    usuario = input("'r' para piedra, 'p' para papel, 's' para tijera: ")
    computadora = random.choice(['r', 'p', 's'])

    if usuario == computadora:
        return 'Empate'
    
    if es_ganador(usuario, computadora):
        return '¡Ganaste!'
    
    return 'Perdiste'

def es_ganador(jugador, oponente):
    if (jugador == 'r' and oponente == 's') or (jugador == 's' and oponente == 'p') \
    or (jugador == 'p' and oponente == 'r'):
        return True

print(jugar())
