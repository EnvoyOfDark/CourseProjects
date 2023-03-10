import random

HANGMAN = [
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    """
]


def get_random_word():
    words = ['python', 'hangman', 'programming', 'code', 'computer']
    return random.choice(words)


def display_board(hidden_word, tries):
    print(HANGMAN[tries])
    print('')
    print(hidden_word)
    print('==='*len(hidden_word))


def get_guess(used_letters):
    while True:
        guess = input('Guess a letter: ').lower()
        if guess.isalpha() and len(guess) == 1:
            if guess in used_letters:
                print('You already used that letter, try again.')
            else:
                return guess
        else:
            print('Invalid input, try again.')


def play_game():
    word = get_random_word()
    hidden_word = '-' * len(word)
    tries = 0
    used_letters = []

    while True:
        display_board(hidden_word, tries)
        guess = get_guess(used_letters)
        used_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word = hidden_word[:i] + guess + hidden_word[i+1:]
            if '-' not in hidden_word:
                print('Congratulations, you win! The word was', word)
                break
        else:
            print('Sorry, the letter is not in the word.')
            tries += 1
            if tries == len(HANGMAN)-1:
                display_board(hidden_word, tries)
                print('Game over, you lose! The word was', word)
                break

        if tries == len(HANGMAN):
            display_board(hidden_word, tries)
            print('Game over, you lose! The word was', word)
            break


if __name__ == '__main__':
    play_game()

