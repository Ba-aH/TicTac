# initialize the board
board = [' ' for x in range(9)]

# function to print the board
def print_board():
    row1 = '|{}|{}|{}|'.format(board[0], board[1], board[2])
    row2 = '|{}|{}|{}|'.format(board[3], board[4], board[5])
    row3 = '|{}|{}|{}|'.format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# function to check if there's a winner
def check_winner(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

# function to play the game
def play_game_x():
    print("Welcome to Tic Tac Toe!")
    print_board()
    player = 'X'

    while True:
        position = int(input("Enter a position (1-9) to place {}: ".format(player)))
        if board[position-1] == ' ':
            board[position-1] = player
            print_board()

            if check_winner(board, player):
                print("{} wins! Congratulations!".format(player))
                break

            if ' ' not in board:
                print("It's a tie!")
                break

            if player == 'X':
                player = 'O'
            else:
                player = 'X'

        else:
            print("That position is already taken. Please choose another position.")


def play_game_o():
    print("Welcome to Tic Tac Toe!")
    print_board()
    player = 'X'

    while True:
        position = int(input("Enter a position (1-9) to place {}: ".format(player)))
        if board[position-1] == ' ':
            board[position-1] = player
            print_board()

            if check_winner(board, player):
                print("{} wins! Congratulations!".format(player))
                break

            if ' ' not in board:
                print("It's a tie!")
                break

            if player == 'X':
                player = 'O'
            else:
                player = 'X'

        else:
            print("That position is already taken. Please choose another position.")

# start the game
play_game()
