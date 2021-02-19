import getpass
import string
from time import sleep

def display_table():
    '''Display game stats'''
    in_file = open('resources/game.txt', 'r')
    content = in_file.read()
    print(content)
    in_file.close()

def check_duplicate(element_list):
    '''Checks if given list has any duplicate'''
    if len(element_list) == len(set(element_list)):
        return False
    else:
        return True

def verify_key(secret):
    '''Verify player Key'''
    if len(secret) != 5 or (not secret.isdigit()):
        return False
    return True

def add_to_record(p1, p2, winner):
    in_file = open('resources/records.txt', 'a+', encoding='utf-8')
    in_file.write('\nPlayer1: '+ p1 + '\nPlayer2: '+ p2 + '\nWinner: 🏆' + winner + '🏆\n' + ('_'*26))
    in_file.close()

def start_game():

    fpl_list = []
    spl_list = []
    move1_ls = []
    move2_ls = []
    dead_o = 0
    dead_t = 0

    print('Hello, Please Choose Turns')

    print('1.Choose Player 1')
    player1 = input("name:> ")
    # REDUCE DUPLICITY
    isValid = False
    while not isValid:       
        secret1 = getpass.getpass(prompt='5-digit secret key>')
        fpl_list = list(secret1)
        if(not verify_key(secret1)):
            print('Invalid number entered!')
            if(check_duplicate(fpl_list)):
                print('Duplicate number found!')
        else:
            isValid = True

    print('2.Choose Player 2')
    player2 = input("name:> ")
    if player1 == player2:
        print('Both players cant bear the same name...')
        player2 = input('new name:>')
    isValid = False
    while not isValid:       
        secret2 = getpass.getpass(prompt='5-digit secret key>')
        spl_list = list(secret2)
        if(not verify_key(secret2)):
            print('Invalid number entered!')
            if(check_duplicate(spl_list)):
                print('Duplicate number found!')
        else:
            isValid = True

    # Create Game Header
    row ='      '+player1+' | '+player2+'\n'+('-'*29)
    with open('resources/game.txt', 'w') as f:
        f.write(row)
    f.close()

    print('Alright then!, Player 1 begins...')
    running = True
    while running:
        move1 = input(player1 +"'s turn: ")
        move1_ls = list(move1)

        dead_o=sum(f==s for(f,s) in zip(move1_ls,spl_list))

        row_o ='\n '+ move1 + ' ' + str(dead_o)+'d' + ' ' + str((5-dead_o))+'a | '
        with open('resources/game.txt', 'a+') as f:
            f.write(row_o)
        f.close()
        display_table()

        move2 = input(player2 +"'s turn: ")
        move2_ls = list(move2)
        dead_t=sum(f==s for(f,s) in zip(move2_ls,fpl_list))

        row_o = move2 + ' ' + str(dead_t)+'d' + ' ' + str((5-dead_t))+'a'
        with open('resources/game.txt', 'a+') as f:
            f.write(row_o)
        f.close()
        display_table()
        if dead_o == 5 or dead_t == 5:
            running = False
            break
    winner = player1 if dead_o==5 else player2
    print('*** 🎊🏆 Congratulations ' + winner + ', You have broken the CodeX! ***')
    add_to_record(player1, player2, winner)
    print(player1 +"'s code was: " + secret1)
    print(player2 +"'s code was: " + secret2)
    newgame = input('Would you like to start a new game?[y/n]: ')
    if newgame == 'Y' or newgame == 'y':
        start_game()
    else:
        pass

def view_records():
    in_file = open('resources/records.txt', 'r', encoding='utf-8')
    content = in_file.read()
    print(content)
    in_file.close()
    input('\nHit the [ENTER] key to continue...\n\n')

def show_rules():
    in_file = open('resources/rules.txt', 'r', encoding='utf-8')
    content = in_file.read()
    print(content)
    in_file.close()
    input('\nHit the [ENTER] key to continue...\n\n')

def close_game():
    print('Exiting...')
    quit

class CodeX:
    def __init__(self):
        active=True
        while active:
            print("\r**Welcome to CodeX**")
            print("1.Create Game\n2.View Records\n3.Rules and Guidelines\n4.Exit game")
            choice = int(input("> "))
            if choice == 1:
                start_game()
            elif choice == 2:
                view_records()
            elif choice == 3:
                show_rules()
            elif choice == 4:
                active=False
                close_game()
            else:
                print('Invalid Option!')

if __name__ == '__main__':
    app = CodeX()