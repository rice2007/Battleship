__author__ = 'AmateurHero'

from random import randint


class Board(list):
    def __init__(self):
        super().__init__()
        for i in range(10):
            self.append(["O"] * 10)

    def __repr__(self):
        board = ''
        for row in self:
            board += " ".join(row) + '\n'
        return board


class Coordinate(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return str(self.row) + 'x' + str(self.col)


class Ship:
    sunk = False
    damage = ''

    def __init__(self, row_one, col_one, row_two, col_two):
        self.row_one = row_one
        self.col_one = col_one
        self.row_two = row_two
        self.col_two = col_two

    def __repr__(self):
        print('Location: %sx%s - %sx%s\nDamage:' % (self.row_one, self.col_one, self.row_two, self.col_two))

    def take_damage(self, row, col):
        self.row = row
        self.col = col

    def update_coordinates(self, row_one, col_one, row_two, col_two):
        self.row_one = row_one
        self.row_two = row_two
        self.col_one = col_one
        self.col_two = col_two


class Destroyer(Ship):
    def __init__(self, row_one, col_one, row_two, col_two):
        super(Destroyer, self).__init__(row_one, col_one, row_two, col_two)


class Carrier(Ship):
    pass


class AI():
    destroyer = Ship(-1, -1, -1, -1)
    cruiser = Ship(-1, -1, -1, -1)
    submarine = Ship(-1, -1, -1, -1)
    battleship = Ship(-1, -1, -1, -1)
    carrier = Ship(-1, -1, -1, -1)
    ai_board = Board()

    def __init__(self):
        seed = get_seed()
        print(seed)
        self.place_ship(seed)

    def is_intersecting(self, ship_type):
        if ship_type.row_one is in range(self.destroyer)

    def place_ship(self, seed):
        for size in range(1, 5):
            if size == 1:
                ship_letter = 'd'
                ship_type = self.destroyer
            elif size == 2:
                ship_letter = 'r'
                ship_type = self.cruiser
            elif size == 3:
                ship_letter = 'b'
                ship_type = self.battleship
            else:
                ship_letter = 'a'
                ship_type = self.carrier

            while (seed.row > 9 - size and seed.col > 9 - size) and :
                seed = get_seed()

            print(seed)
            if seed.row >= 9 - size + 1:
                ship_type.update_coordinates(seed.row, seed.col, seed.row, seed.col + size)
                for i in range(ship_type.col_one, ship_type.col_two + 1):
                    self.ai_board[ship_type.row_one][i] = ship_letter
            elif seed.col >= 9 - size + 1:
                ship_type.update_coordinates(seed.row, seed.col, seed.row + size, seed.col)
                for i in range(ship_type.row_one, ship_type.row_two + 1):
                    self.ai_board[i][ship_type.col_one] = ship_letter
            else:
                is_vertical = randint(0, 1)
                if is_vertical == 0:
                    ship_type.update_coordinates(seed.row, seed.col, seed.row, seed.col + size)
                    for i in range(ship_type.col_one, ship_type.col_two + 1):
                        self.ai_board[ship_type.row_one][i] = ship_letter
                else:
                    ship_type.update_coordinates(seed.row, seed.col, seed.row + size, seed.col)
                    for i in range(ship_type.row_one, ship_type.row_two + 1):
                        self.ai_board[i][ship_type.col_one] = ship_letter

            print(self.ai_board)
            seed = get_seed()





def get_seed():
    return Coordinate(randint(0, 9), randint(0, 9))


print("Let's play Battleship!")
game_board = Board()
print(game_board)
ai = AI()
print(ai.ai_board)
turn = 0

# for i in range(4):
#     print("Turn ", turn)
#     guess_row = int(input("Guess Row:"))
#     guess_col = int(input("Guess Col:"))
#
#     if guess_row == ship_row and guess_col == ship_col:
#         print("Congratulations! You sunk my battleship!")
#         break
#     else:
#         if (guess_row not in range(4)) or \
#                 (guess_col not in range(4)):
#             print("Oops, that's not even in the ocean.")
#         elif game_board[guess_row][guess_col] == "X":
#             print("You guessed that one already.")
#         else:
#             print("You missed my battleship!")
#             game_board[guess_row][guess_col] = "X"
#             if turn == 3:
#                 print("Game Over")
#         print_board(game_board)
#     turn += 1

# Make multiple battleships: you'll need to be careful because you need to make sure that you don’t place battleships on
#  top of each other on the game board. You'll also want to make sure that you balance the size of the board with the
#  number of ships so the game is still challenging and fun to play.
#
# Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be
#  vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the
#  side of the board.
#
# Make your game a two-player game.
#
# Use functions to allow your game to have more features like rematches, statistics and more!