
import random

def play():
    user = input("'r' for rock, 'p' for paper,'s' for scissor")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'tie'
    
    if is_win(user,computer):
        return 'you won'
    
    return 'you lost'

def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent =='r'):
        return True

play()