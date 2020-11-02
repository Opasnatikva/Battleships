import string

BOARD_SIZE = 10
BLANK_STATE = " "
HIT_BLANK_FIELD = "*"
SHIP_FIELD = "+"
HIT_SHIP_FIELD = "X"
player_one = True
nation = ["usa", "ussr"]
board_type = ["ships", "shots"]
ships = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}
used_ships = []


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
    for index in nation:
        boards[index] = {}
        for boardtype in board_type:
            boards[index][boardtype] = generate_board()
    return boards


def user_input(ships = ships):
    ship_name = input("Please choose the ship you would like to place! Your options are " + str(list(ships.keys())))
    ship_type = ships[ship_name]
    orient = input("Would you like to ship to be vertically or horizontally positioned, commander? Please type \"h\" for horizontal, or \"v\" for vertical!")
    if orient == "h":
        coors = input("Please provide us with coordinates for the ship, commander! The ship will be placed to the right starting at the provided value.")
    else:
        coors = input("Please provide us with coordinates for the ship, commander! The ship will be placed downwards from the provided value.")
    key = coors[0]
    line_index = int(coors[1])
    return ship_type, key, line_index


def placement_check(ship_type, orientation, row, column, player):
    # Boundary check
    if orientation == "h":
        if string.ascii_uppercase.index(row) + ship_type > BOARD_SIZE:
            return False
    else:
        if column + (ship_type - 1) > BOARD_SIZE:
            return False
    if player:
        player_board = "usa"
    else:
        player_board = "ussr"
    if orientation == "h":
        for field in boards[player_board]["ships"][row][column - 1:column - 1 + ship_type]:
            if field == SHIP_FIELD:
                print("A ship already occupies one or more of those fields, commander!")
                return False
    else:
        start = string.ascii_uppercase.index(row)
        for line in string.ascii_uppercase[start:start + ship_type]:
            if boards[player_board]["ships"][line][column] == SHIP_FIELD:
                print("A ship already occupies one or more of those fields, commander!")
                return False
    return True


def place_ship(ship_type, player, orientation, row, column):
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
boards["usa"]["ships"]["G"][6] = SHIP_FIELD
ship_len = 5
orient = "v"
row_row = "F"
col_col = 6
if placement_check(ship_len, orient, row_row, col_col, True):
    place_ship(ship_len, player_one, orient, row_row, col_col)
else:
    print("Please give us different coordinates sir!")
print_both_boards()
# while True:
#     print_both_boards()
#
#
#
#     player_one = not player_one
