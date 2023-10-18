import random
import palabras as p
import string

def get_valid_word(p):
    word = random.choice(p)
    while '-' in word or ' ' in word:
        word = random.choice(p)
    
    return word
    
def hangman():
    word = get_valid_word(p)
    word_letters = set(word)
    alphbet = set(string.ascii_uppercase)
