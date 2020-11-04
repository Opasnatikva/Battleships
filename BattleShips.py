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
        for board_type in BOARD_TYPE:
            boards[index][board_type] = generate_board()
    return boards


def print_both_boards(player):
    if player:
        player_board = NATION[0]
    else:
        player_board = NATION[1]
    print_board(boards[player_board][BOARD_TYPE[0]])
    print_board(boards[player_board][BOARD_TYPE[1]])


def user_input():
    correct_input = False
    coors = ''
    orient = ''
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
    logical_column = int(coors[1:]) - 1
    return orient, key, logical_column


def input_and_check(board, ship_type, player):
    input_correct = False
    orientation = ''
    row = ''
    logical_column = ''
    while not input_correct:
        orientation, row, logical_column = user_input()
        input_correct = placement_check(board, ship_type, orientation, row, logical_column, player)
    return orientation, row, logical_column


def placement_check(boards, ship_type, orientation, row, logical_column, player):
    # Boundary check
    if orientation == "h":
        if logical_column + ship_type > BOARD_SIZE:
            return False
    else:
        if string.ascii_uppercase.index(row) + ship_type > BOARD_SIZE:
            return False
    if player:
        player_board = NATION[0]
    else:
        player_board = NATION[1]
    #     Collision check
    if orientation == "h":
        for cell in range(logical_column, logical_column + ship_type):
            if boards[player_board][BOARD_TYPE[0]][row][cell] == SHIP_FIELD:
                return False
    else:
        start = string.ascii_uppercase.index(row)
        stop = start + ship_type - 1
        for key in string.ascii_uppercase[start:stop]:
            if boards[player_board][BOARD_TYPE[0]][key][logical_column] == SHIP_FIELD:
                return False
    return True


def place_ship(boards, player, ship_type, orientation, row, logical_column):
    if player:
        board = boards[NATION[0]][BOARD_TYPE[0]]
    else:
        board = boards[NATION[1]][BOARD_TYPE[0]]
    if orientation == "h":
        for col_index in range(logical_column, logical_column + ship_type):
            board[row][col_index] = SHIP_FIELD
    else:
        start = string.ascii_uppercase.index(row)
        for row_index in string.ascii_uppercase[start:start + ship_type]:
            board[row_index][logical_column] = SHIP_FIELD


def user_hit_input():
    correct_input = False
    coors = ''
    while not correct_input:
        coors = input("Point us towards the target, captain!")
        coors = coors.upper()
        if 1 < len(coors) < 4 and coors[0] in string.ascii_uppercase[0:10] and coors[1:].isdigit() and 0 < int(
                coors[1:]) <= 10:
            correct_input = True
        else:
            print("Please insert correct coordinates!")
    return coors


def already_hit(board, key, logical_column):
    if board[key][logical_column] is not HIT_SHIP_FIELD and not HIT_BLANK_FIELD:
        return True
    return False


def place_hit(board, key, logical_column):
    if board[key][logical_column] == SHIP_FIELD:
        board[key][logical_column] = HIT_SHIP_FIELD
    else:
        board[key][logical_column] = HIT_BLANK_FIELD


def fire_weapons(boards, player):
    if player:
        ship_board = boards[NATION[1]][BOARD_TYPE[0]]
        shot_board = boards[NATION[0]][BOARD_TYPE[1]]
    else:
        ship_board = boards[NATION[0]][BOARD_TYPE[0]]
        shot_board = boards[NATION[1]][BOARD_TYPE[1]]
    correct_input = False
    key = ''
    col_index = ''
    while not correct_input:
        coordinates = user_hit_input()
        key = coordinates[0]
        col_index = int(coordinates[1:]) - 1
        if not already_hit(ship_board, key, col_index):
            correct_input = True
    place_hit(ship_board, key, col_index)
    place_hit(shot_board, key, col_index)


def game_over(boards, player_one):
    if player_one:
        player_board = NATION[1]
    else:
        player_board = NATION[0]
    for value in boards[player_board][BOARD_TYPE[0]].values():
        for element in value:
            if element == SHIP_FIELD:
                return False
    return True


def win_announcement(player):
    if player:
        winner = NATION[0]
    else:
        winner = NATION[1]
    print("Congratulations " + winner + "! You have vanquished all of the enemy\'s ships!")


def main():
    pass


if __name__ == '__main__':
    main()
#
# boards = generate_initial_boards()
# ship_type = 5
# orient = "h"
# row_row = "C"
# col_col = 0
# if placement_check(boards, ship_type, orient, row_row, col_col, True):
#     place_ship(boards, player_one, ship_type, orient, row_row, col_col)
# else:
#     print("No can do sir!1")
# ship_type = 5
# orient = "v"
# row_row = "A"
# col_col = 4
# if placement_check(boards, ship_type, orient, row_row, col_col, True):
#     place_ship(boards, player_one, ship_type, orient, row_row, col_col)
# else:
#     print("No can do sir!2")
# print_both_boards()

boards = generate_initial_boards()
for index in range(2):
    for value in SHIPS.values():
        print_both_boards(player_one)
        orientation, row, logical_column = input_and_check(boards, value, player_one)
        place_ship(boards, player_one, value, orientation, row, logical_column)
    player_one = not player_one
while not game_over(boards, player_one):
    print_both_boards(player_one)
    fire_weapons(boards, player_one)
    game_over(boards, player_one)
    player_one = not player_one
win_announcement(player_one)
