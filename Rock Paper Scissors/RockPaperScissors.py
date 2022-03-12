import random
# a simple rock paper scissors game against the computer

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r','p', 's'])

    if user == computer:
        return 'Tied'
    if is_win(user, computer):
        return 'You won.'
    return 'You lost.'

def is_win (player, opponent):
    if (player == ' r' and opponent == 's') or (player == 's' and opponent =='p') or \
            (player == 'p' and opponent == ' r'):
        return True

print(play())
