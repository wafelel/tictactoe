from random import randint
from subprocess import call

def print_board(board):
    row_number = 1
    for row in board:
        print(row_number, end=" ")
        row_number += 1
        for slot in row:
            print(slot, end=" ")
        print("")
    print("  A B C" )

def move(coords, board, player_token):
    x = int(coords[0]) - 1
    def letter_to_number(letter):
        if letter == "A":
            return 0
        elif letter == "B":
            return 1
        elif letter == "C":
            return 2
    y = letter_to_number(coords[1].upper())
    if board[x][y] == "-":
        board[x][y] = player_token
        return True
    else:
        return False

def change_token(player_token):
    if player_token == "x":
        return "o"
    elif player_token == "o":
        return "x"

def check_for_winner(board):
    def check_rows(board):
        for row in board:
            if row.count("x") == 3:
                return "x"
            elif row.count("o") == 3:
                return "o"
    def check_columns(board):
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i]:
                if board[0][i] == "x":
                    return "x"
                elif board[0][i] == "o":
                    return "o"
    def check_diagonals(board):
        if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
            if board[1][1] == "x":
                return "x"
            elif board[1][1] == "o":
                return "o"

    return check_rows(board) or check_columns(board) or check_diagonals(board)

def main():
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    if randint(0, 1) == 0:
        player = "x"
    else:
        player = "o"
    while True:
        call(["clear"])
        print_board(board)
        print("Now " + player + " moves")
        coords = input("Where do you want to move? Ie 1A\n")
        if not move(coords, board, player):
            print("You can't do this!")
            continue
        winner = check_for_winner(board)
        if winner:
            call(["clear"])
            print_board(board)
            print(winner + " has won!")
            break
        player = change_token(player)

if __name__ == "__main__":
    main()