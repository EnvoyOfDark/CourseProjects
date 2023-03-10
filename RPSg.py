import random


def play_game():

    infinity = True

    while infinity:
        player_choice = input('Player choise: [Rock/Paper/Scissors]\n').lower()

        if player_choice not in ['rock', 'paper','scissors']:
            print('Incorrect input. Try again')
            continue
        comp_choice = random.choice(['rock', 'paper','scissors'])

        print(f'Comp choice = {comp_choice}')
        win_comb = [('paper','rock'), ('rock', 'scissors'), ('scissors', 'paper')]

        if player_choice == comp_choice:
            print('A draw!')
        elif (player_choice, comp_choice) in win_comb:
            print('Player wins!')
        else:
            print('Comp wins!')

        infinity = input('Want to proceed? [y/n]\n').lower() == 'y'


if __name__ == '__main__':
    game = play_game()