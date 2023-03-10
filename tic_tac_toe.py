def print_board(board):
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")


def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


def tic_tac_toe():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    players = ["X", "O"]
    current_player = players[0]
    game_over = False

    while not game_over:
        print_board(board)
        print(f"It's {current_player}'s turn")

        move = input("Enter position (1-9): ")
        move = int(move) - 1

        if board[move] == " ":
            board[move] = current_player

            if check_win(board, current_player):
                print_board(board)
                print(f"{current_player} wins!")
                game_over = True
            elif " " not in board:
                print_board(board)
                print("Tie game!")
                game_over = True
            else:
                current_player = players[1] if current_player == players[0] else players[0]
        else:
            print("Position already taken, try again.")


if __name__ == '__main__':
    tic_tac_toe()