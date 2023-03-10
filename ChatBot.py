from NewOne import tic_tac_toe, Hangman, RPSg, bj
import pyjokes


def interface():
    command = input("""Welcome to simple ChatBot!\n
    Menu:
    1 - Find movie by genre
    2 - Play Games
    3 - Get a random joke\n
Make your choise: """)
    match command:
        case '1': find_movie()
        case '2': play_games()
        case '3': get_joke()
        case _: 'Incorrect input. Try again.'


def find_movie():
    print('''\nAvaliable genres: 
    Comedy, Family, Short, Romance, Drama, Talk-Show, Animation, Romance, Adventure,
    Fantasy, Music, Action, Game-Show, Sci-Fi, Crime, News,	Musical, Reality-TV, Mystery, Horror, Thriller, 
    Documentary, Sport, History, Western, War, Biography, Film-Noir, Adult\n''')
    row_search = input('What movie genre would you like to find: ').title()
    search = row_search.replace(' ', '+')
    link = f'https://www.imdb.com/search/title/?genres={row_search}&explore=title_type,genres&ref_=adv_explore_rhs'
    print(f'Please follow this link: {link}')


def get_joke():
    print(pyjokes.get_joke('en', 'all'))


def play_games():
    game = input("""\nGames list:
    1 - Tic-Tac-Toe
    2 - Hangman
    3 - Rock Paper Scissors
    4 - Black Jack\n
Make your choise: """)
    match game:
        case '1': tic_tac_toe.tic_tac_toe()
        case '2': Hangman.play_game()
        case '3': RPSg.play_game()
        case '4': bj.Game().play_game()
        case _: 'Incorrect input. Try again.'


while True:
    print()
    interface()