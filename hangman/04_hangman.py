import random
import string

# Assume the 'palabras' module contains a list of words named 'p'
from palabras import words

def obtener_palabra_valida(lista_de_palabras):
    palabra = random.choice(lista_de_palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(lista_de_palabras)
    
    return palabra

def ahorcado():
    palabra = obtener_palabra_valida(words)
    letras_de_la_palabra = set(palabra)
    alfabeto = set(string.ascii_uppercase)
    used_letters = set()

    while len(letras_de_la_palabra) > 0:
        # letters used
        # ''.join(['a','b','cd']) --> 'a b cd'
        print('you have used these letters: ', ' '.join(used_letters))

        #what current word is (ie W - R D)
        word_list = [ letter if letter in used_letters else '-' for letter in palabra]
        print('current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter:  ').upper()
        if user_letter in alfabeto - used_letters:
            used_letters.add(user_letter)
            if user_letter in letras_de_la_palabra:
                letras_de_la_palabra.remove(user_letter)
        elif user_letter in used_letters:
            print('you have already used that character. please try again')
        else:
            print('Invalid character. please try again')
    # gets here when len(letras_de_la_palabra) == 0


ahorcado()