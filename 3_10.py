# board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
# checking if game is still going on
game_still_on = True

# who won?who tie
winner = None

# whos turn?
current_player = "x"


# displaying board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turn():
    print(current_player + "'s turn.")
    position = (input("choose a position from 1-9-"))

    valid = False
    while not valid:
        while position not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            position = input("plz enter a position from 1-9 ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("oops! you cant go there .try again!")

    board[(position)] = current_player
    display_board()


def check_if_gameover():
    check_if_win()
    check_if_tie()
    return


def check_if_win():
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonal
    diagonal_winner = check_diagonal()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    # setup global variables
    global game_still_on
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_on = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return


def check_columns():
    # setup global variables
    global game_still_on
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_on = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonal():
    # setup global variables
    global game_still_on
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_on = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


def check_if_tie():
    global game_still_on
    if "-" not in board:
        game_still_on = False
    return


def flip_player():
    global current_player
    if current_player == "x":
        current_player = "o"
    elif (current_player == "o"):
        current_player = "x"
    return


# main start game display
def play_game():
    # initial board
    display_board()
    while game_still_on:
        handle_turn()
        check_if_gameover()
        flip_player()


play_game()
# end of game
if (winner == "x" or winner == "0"):
    print(winner + " won")
elif (winner == None):
    print("tie")
