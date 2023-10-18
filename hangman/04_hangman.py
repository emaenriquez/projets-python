import random
import palabras as p
import string

def obtener_palabra_valida(lista_de_palabras):
    palabra = random.choice(lista_de_palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(lista_de_palabras)
    
    return palabra

def ahorcado():
    palabra = obtener_palabra_valida(p)  # Obtiene una palabra válida de la lista "p"
    letras_de_la_palabra = set(palabra)  # Convierte la palabra en un conjunto de letras únicas
    alfabeto = set(string.ascii_uppercase)  # Crea un conjunto de letras del alfabeto en mayúsculas
    used_letters = set()

    user_letter = input('Guess a letter:  ').upper()
    if user_letter in alfabeto - used_letters:
        used_letters.add(user_letter)
        if user_letter in letras_de_la_palabra:
            letras_de_la_palabra.remove(user_letter)
    elif user_letter in used_letters:
        print('you have already used that character. please try again')
    else:
        print('')

user_input = input('Type somethig')

print(user_input)