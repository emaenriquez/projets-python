import random

# Adivina el número (computadora)
def adivina_numero(x):
    numero_aleatorio = random.randint(1, x)
    suposicion = 0
    while suposicion != numero_aleatorio:
        suposicion = int(input(f'Adivina un número entre 1 y {x}: '))
        if suposicion < numero_aleatorio:
            print('Lo siento, intenta de nuevo, es demasiado bajo.')
        elif suposicion > numero_aleatorio:
            print('Lo siento, intenta de nuevo, es demasiado alto.')
    print(f'¡Yay, felicidades! Adivinaste el número {numero_aleatorio}.')


# Adivina el número (usuario)
def adivina_numero_computadora(x):
    bajo = 1
    alto = x
    feedback = ''
    while feedback != 'c' and bajo <= alto:
        if bajo <= alto:
            suposicion = random.randint(bajo, alto)
        else:
            suposicion = bajo

        feedback = input(f'¿Es {suposicion} demasiado alto (H), demasiado bajo (L), o correcto (C)? ').lower()
        
        if feedback == 'h':
            alto = suposicion - 1
        if feedback == 'l':
            bajo = suposicion + 1

    print(f'¡Yay, la computadora adivinó tu número, {suposicion}, correctamente!')

adivina_numero_computadora(4)
