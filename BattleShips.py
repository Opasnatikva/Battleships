import string

BOARD_SIZE = 10
BLANK_STATE = " "
HIT_BLANK_FIELD = "*"
SHIP_FIELD = "+"
HIT_SHIP_FIELD = "X"
NATION = ["usa", "ussr"]
BOARD_TYPE = ["ships", "shots"]
SHIPS = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}
player_one = True


# orientation = input("Please choose the orientation of your ship! Type \"H\" for horizontal or \"V\" for vertical)!")


def generate_board(size=BOARD_SIZE):
    board = {}
    for letter in string.ascii_uppercase[:size]:
        board[letter] = []
        for index in range(size):
            board[letter].append(BLANK_STATE)
    return board


def print_board(board):
    top_line = []
    for index in range(BOARD_SIZE):
        top_line.append(str(index + 1))
    print(" ", top_line)
    for key in board.keys():
        print(key, board[key])


def generate_initial_boards():
    boards = {}
    for index in NATION:
        boards[index] = {}
        for boardtype in BOARD_TYPE:
            boards[index][boardtype] = generate_board()
    return boards


def user_input():
    correct_input = False
    while not correct_input:
        orient = input(
            "Would you like your " + "carrier" + " to be vertically or horizontally positioned, commander? Please type \"h\" for horizontal, or \"v\" for vertical!")
        orient = orient.lower()
        if orient == 'h' or orient == 'v':
            correct_input = True
        else:
            print("Please insert correct orientation!")
    correct_input = False
    if orient == 'h':
        message = "Please provide us with coordinates for the " + "carrier" + ", commander! The ship will be placed to the right starting at the provided value. For example \"A1\""
    else:
        message = "Please provide us with coordinates for the " + "carrier" + ", commander! The ship will be placed downwards from the provided value. For example \"A1\"."
    while not correct_input:
        coors = input(message)
        coors = coors.upper()
        if 1 < len(coors) < 4 and coors[0] in string.ascii_uppercase[0:10] and coors[1:].isdigit() and 0 < int(
                coors[1:]) <= 10:
            correct_input = True
        else:
            print("Please insert correct coordinates!")
    key = coors[0]
    line_index = int(coors[1:])
    return orient, key, line_index


def input_and_check(board, ship_type, player = True):
    input_correct = False
    while not input_correct:
        orientation, row, column = user_input()
        input_correct = placement_check(board, ship_type, orientation, row, column, player)
    return orientation, row, column

def placement_check(board, ship_type, orientation, row, column, player):
    # Boundary check
    if orientation == "h":
        if column + (ship_type - 1) > BOARD_SIZE:
            return False
    else:
        if string.ascii_uppercase.index(row) + ship_type > BOARD_SIZE:
            return False
    if player:
        player_board = "usa"
    else:
        player_board = "ussr"
    if orientation == "h":
        for cell in range(column - 1, column - 1 + ship_type):
            if boards[player_board]["ships"][row][cell] == SHIP_FIELD:
                return False
    else:
        start = string.ascii_uppercase.index(row)
        stop = start + ship_type - 1
        for key in string.ascii_uppercase[start:stop]:
            if boards[player_board]["ships"][key][column] == SHIP_FIELD:
                return False
    return True


def place_ship(boards, player, ship_type, orientation, row, column):
    if player:
        board = boards["usa"]["ships"]
    else:
        board = boards["ussr"]["ships"]
    if orientation == "h":
        for col_index in range(column - 1, column + ship_type - 1):
            board[row][col_index] = SHIP_FIELD
    else:
        start = string.ascii_uppercase.index(row)
        for row_index in string.ascii_uppercase[start:start + ship_type]:
            board[row_index][column - 1] = SHIP_FIELD


def print_both_boards(player=player_one):
    if player:
        player_board = "usa"
    else:
        player_board = "ussr"
    print_board(boards[player_board]["ships"])
    print_board(boards[player_board]["shots"])


def hit():
    pass


def main():
    pass


if __name__ == '__main__':
    main()

boards = generate_initial_boards()
ship_type = 5
orient = "h"
row_row = "C"
col_col = 1
if placement_check(boards, ship_type, orient, row_row, col_col, True):
    place_ship(boards,  player_one,ship_type, orient, row_row, col_col)
else:
    print("No can do sir!1")
ship_type = 5
orient = "v"
row_row = "A"
col_col = 5
if placement_check(boards, ship_type, orient, row_row, col_col, True):
    place_ship(boards, player_one, ship_type, orient, row_row, col_col)
else:
    print("No can do sir!2")
print_both_boards()
print(input_and_check(boards, 5))
# boards = generate_initial_boards()
#
# while True:
#     print_both_boards()
#
#     player_one = not player_one


# Collision between ships need to debug the finction that checks for previously placed ones