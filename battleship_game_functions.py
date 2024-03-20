# Constants that describe the limits on ship sizes and grid sizes.
MIN_SHIP_SIZE = 1
MAX_SHIP_SIZE = 10
MAX_GRID_SIZE = 10

# Constants that describe valid grid cell values (other than ship symbols).
EMPTY = '.'
UNKNOWN = '-'
HIT = 'X'
MISS = 'M'


# Implement the required functions below according to their docstrings.
#
# We have provided the complete docstring (but not the body!) for each of the
# functions that you are to complete.  When you have completed all of the
# functions, run the file play_battleship_game.py to play the game!


def valid_cell_indexes(row: int, col: int, grid_size: int) -> bool:
    """Return True if and only if row and col are between 0 (inclusive) and
    grid_size (non-inclusive).

    >>> valid_cell_indexes(2, 9, 10)
    True
    >>> valid_cell_indexes(2, 9, 9)
    False
    """
    return 0 <= row < grid_size and 0 <= col < grid_size


def is_not_given_symbol(row: int, col: int, grid: list[list[str]],
                        symbol: str) -> bool:
    """Return True if and only if the grid cell with row position row and
    column position col is NOT symbol.

    Preconditions:
        - 0 <= row < len(grid)
        - 0 <= col < len(grid)
        - 0 < len(grid)
        - len(grid[i]) == len(grid)
              for each value of i in range(len(grid))

    >>> my_grid = [['a', UNKNOWN], [UNKNOWN, 'b']]
    >>> is_not_given_symbol(1, 1, my_grid, UNKNOWN)
    True
    >>> is_not_given_symbol(0, 1, my_grid, UNKNOWN)
    False
    """
    return grid[row][col] != symbol


def is_win(ship_sizes: list[int], hits_list: list[int]) -> bool:
    """Return True if and only if hits_list contains the same values as
    ship_sizes, in the same order.

    ship_sizes and hits_list are parallel lists.

    Preconditions:
       - len(ship_sizes) == len(hits_list)

    >>> is_win([1, 2, 3], [1, 2, 3])
    True
    >>> is_win([1, 2, 3], [1, 2, 0])
    False
    """
    return ship_sizes == hits_list


def update_target_grid(row: int, col: int, target_grid: list[list[str]],
                       fleet_grid: list[list[str]]) -> None:
    """Modify the cell with row position row and column position col in
    target_grid to either HIT or MISS by using the information in the
    corresponding cell from fleet_grid.

    Preconditions:
        - 0 <= row < len(target_grid)
        - 0 <= col < len(target_grid)
        - 0 < len(target_grid)
        - len(target_grid[i]) == len(target_grid)
              for each value of i in range(len(target_grid))
        - len(fleet_grid) == len(target_grid)
        - len(fleet_grid[i]) == len(fleet_grid)
              for each value of i in range(len(fleet_grid))

    >>> my_target_grid = [[UNKNOWN, UNKNOWN], [UNKNOWN, UNKNOWN]]
    >>> their_fleet_grid = [['a', 'b'], ['a', EMPTY]]
    >>> update_target_grid(1, 1, my_target_grid, their_fleet_grid)
    >>> my_target_grid == [[UNKNOWN, UNKNOWN], [UNKNOWN, MISS]]
    True
    >>> my_target_grid = [[UNKNOWN, UNKNOWN], [UNKNOWN, UNKNOWN]]
    >>> their_fleet_grid = [[EMPTY, EMPTY], [EMPTY, 'a']]
    >>> update_target_grid(1, 1, my_target_grid, their_fleet_grid)
    >>> my_target_grid == [[UNKNOWN, UNKNOWN], [UNKNOWN, HIT]]
    True
    """
    if fleet_grid[row][col] == EMPTY:
        target_grid[row][col] = MISS
    else:
        target_grid[row][col] = HIT


def update_fleet_grid(row: int, col: int, fleet_grid: list[list[str]],
                      ship_symbols: list[str], hits_list: list[int]) -> None:
    """Modify hits_list and fleet_grid to account for a hit of the cell
    at row position row and column position col.  Convert the correct cell
    in fleet_grid to upper case and increase the corresponding count in
    hits_list by one.

    ship_symbols and hits_list are parallel lists.

    Preconditions:
        - 0 <= row < len(fleet_grid)
        - 0 <= col < len(fleet_grid)
        - 0 < len(fleet_grid)
        - len(fleet_grid[i]) == len(fleet_grid)
              for each value of i in range(len(fleet_grid))
        - len(ship_symbols) == len(hits_list) and 0 < len(ship_symbols)
        - fleet_grid[row][col] in ship_symbols

    >>> my_hits_list = [0]
    >>> my_fleet_grid = [[EMPTY, 'a'], [EMPTY, 'a']]
    >>> update_fleet_grid(0, 1, my_fleet_grid, ['a'], my_hits_list)
    >>> my_hits_list == [1]
    True
    >>> my_fleet_grid == [[EMPTY, 'A'], [EMPTY, 'a']]
    True
    """
    ship_index = ship_symbols.index(fleet_grid[row][col])
    hits_list[ship_index] += 1
    fleet_grid[row][col] = fleet_grid[row][col].upper()


def get_ship_symbol_count(fleet_grid: list[list[str]],
                          ship_symbol: str) -> int:
    """Return the number of occurrences of ship_symbol in fleet_grid.

    Preconditions:
        - 0 < len(fleet_grid)
        - len(fleet_grid[i]) == len(fleet_grid)
              for each value of i in range(len(fleet_grid))
        - len(ship_symbol) == 1

    >>> grid = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
    >>> get_ship_symbol_count(grid, 'c')
    3
    >>> grid = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'i', 'j']]
    >>> get_ship_symbol_count(grid, 'k')
    0
    """


def has_ship(fleet_grid: list[list[str]], row_start: int, col_start: int,
             ship_symbol: str, ship_size: int) -> bool:
    """Return True if and only if a ship that (1) uses ship_symbol as its ship
    symbol and (2) has length ship_size appears in fleet_grid starting at
    position (row_start, col_start), where (row_start, col_start) is the
    top-most/left-most corner of the ship.

    If the ship has ship_size 2 or more and appears as both a column and a row,
    return False.

    Preconditions:
        - 0 < len(fleet_grid)
        - len(fleet_grid[i]) == len(fleet_grid)
              for each value of i in range(len(fleet_grid))
        - 0 <= row_start < len(fleet_grid)
        - 0 <= col_start < len(fleet_grid)
        - MIN_SHIP_SIZE <= ship_size <= MAX_SHIP_SIZE
        - fleet_grid[i][j] != ship_symbol for each of the coordinates
             (i, j) == (row_start - 1, col_start) or
             (i, j) == (row_start, col_start - 1)
             when those coordinates are valid indexes for fleet_grid
 
    >>> grid = [[EMPTY, 'b', EMPTY], ['a', 'b', EMPTY], [EMPTY, EMPTY, EMPTY]]
    >>> has_ship(grid, 0, 1, 'b', 2)
    True
    >>> has_ship(grid, 0, 1, 'b', 1)
    False
    >>> has_ship(grid, 0, 1, 'b', 3)
    False
    >>> has_ship(grid, 1, 0, 'a', 1)
    True
    >>> grid = [['b', 'b', 'b'], ['b', EMPTY, EMPTY], ['b', EMPTY, EMPTY]]
    >>> has_ship(grid, 0, 0, 'b', 3)
    False
    """


def validate_symbol_counts(fleet_grid: list[list[str]],
                           ship_symbols: list[str],
                           ship_sizes: list[int]) -> bool:
    """Return True if and only if fleet_grid contains each ship symbol in
    ship_symbols the correct corresponding number of times from ship_sizes,
    and nothing else except for the EMPTY character.

    ship_symbols and ship_sizes are parallel lists.

    Note: This function does not consider whether ship symbols are positioned
    in an appropriate manner to form a complete ship.  It simply validates the
    symbol counts.

    Preconditions:
        - 0 < len(fleet_grid)
        - len(fleet_grid[i]) == len(fleet_grid)
              for each value of i in range(len(fleet_grid))
        - len(ship_symbols) == len(ship_sizes) and 0 < len(ship_symbols)
        - len(ship_symbols[i]) == 1
              for each value of i in range(len(ship_symbols))
        - 1 <= len(ship_sizes[i])
              for each value of i in range(len(ship_sizes))

    >>> grid = [[EMPTY, 'b', EMPTY], [EMPTY, 'b', EMPTY], ['a', 'a', 'a']]
    >>> ships = ['a', 'b']
    >>> sizes = [3, 2]
    >>> validate_symbol_counts(grid, ships, sizes)
    True
    >>> grid = [['b', EMPTY, EMPTY], [EMPTY, 'b', 'a'], ['a', 'a', EMPTY]]
    >>> ships = ['a', 'b']
    >>> sizes = [3, 2]
    >>> validate_symbol_counts(grid, ships, sizes)
    True
    >>> grid = [['d', 'a', 'n'], [EMPTY, 'i', 's'], ['f', 'i', 't']]
    >>> ships = ['a', 'd', 'f', 'i', 'n']
    >>> sizes = [1, 1, 1, 2, 1]
    >>> validate_symbol_counts(grid, ships, sizes)
    False
    """


def validate_ship_positions(fleet_grid: list[list[str]],
                            ship_symbols: list[str],
                            ship_sizes: list[int]) -> bool:
    """Return True if and only if fleet_grid contains each ship in ship_symbols
    the correct corresponding number of times from ship_sizes, with ship
    characters all connected in a single row or column.

    ship_symbols and ship_sizes are parallel lists.

    Preconditions:
        - 0 < len(fleet_grid)
        - len(fleet_grid[i]) == len(fleet_grid)
              for each value of i in range(len(fleet_grid))
        - len(ship_symbols) == len(ship_sizes) and 0 < len(ship_symbols)
        - len(ship_symbols[i]) == 1
              for each value of i in range(len(ship_symbols))
        - 1 <= len(ship_sizes[i])
              for each value of i in range(len(ship_sizes))
        - validate_symbol_counts(fleet_grid, ship_symbols, ship_sizes) == TRUE

    >>> grid = [[EMPTY, 'b', EMPTY], [EMPTY, 'b', EMPTY], ['a', 'a', 'a']]
    >>> ships = ['a', 'b']
    >>> sizes = [3, 2]
    >>> validate_ship_positions(grid, ships, sizes)
    True
    >>> grid = [[EMPTY, 'b', EMPTY], [EMPTY, 'b', EMPTY], ['a', 'b', 'a']]
    >>> ships = ['a', 'b']
    >>> sizes = [2, 3]
    >>> validate_ship_positions(grid, ships, sizes)
    False
    """


if __name__ == '__main__':
    # Automatically run all doctest examples to see if any fail
    import doctest
    # uncomment the line below to run the docstring 
    #doctest.testmod()
# The file contains functions that allow for human vs. computer play

from random import randint
from battleship_game_functions import MIN_SHIP_SIZE, MAX_SHIP_SIZE, \
                                      MAX_GRID_SIZE, EMPTY, UNKNOWN
from battleship_game_functions import valid_cell_indexes, is_not_given_symbol



def make_empty_fleet_grid(grid_size: int) -> list[list[str]]:
    """Return a grid_size by grid_size grid containing EMPTY in every cell."""
    fleet_grid = []
    for _ in range(grid_size):
        grid_row = [EMPTY] * grid_size
        fleet_grid.append(grid_row)
    return fleet_grid


def is_occupied(row1: int, col1: int, row2: int, col2: int,
                fleet_grid: list[list[str]]) -> bool:
    """Return True if a cell between (row1, col1) and
    (row2, col2), inclusive, in fleet_grid is not set to the EMPTY symbol."""
    if col1 == col2:
        for row in range(min(row1, row2), max(row1, row2) + 1):
            if fleet_grid[row][col1] != EMPTY:
                return True
    else:
        for col in range(min(col1, col2), max(col1, col2) + 1):
            if fleet_grid[row1][col] != EMPTY:
                return True
    return False


def get_end_indexes(start_row: int, start_col: int, ship_size: int) \
                    -> list[int]:
    """Return the end row and end column based on start_row, start_col, and
    ship_size, for a randomly generated direction."""
    direction = randint(0, 1)
    if direction == 0:
        end_row = start_row
        end_col = start_col + ship_size - 1
    else:
        end_row = start_row + ship_size - 1
        end_col = start_col
    return [end_row, end_col]


def place_ship(row1: int, col1: int, row2: int, col2: int,
               fleet_grid: list[list[str]], ship_symbol: str) -> None:
    """Modify fleet_grid by placing a ship_symbol from (row1, col1) to
    (row2, col2), inclusive."""
    if row1 == row2:
        for col in range(col1, col2 + 1):
            fleet_grid[row1][col] = ship_symbol
    else:
        for row in range(row1, row2 + 1):
            fleet_grid[row][col1] = ship_symbol


def randomly_place_ship(fleet_grid: list[list[str]], ship_symbol: str,
                        ship_size: int) -> bool:
    """Return True if a random attempt to place ship using 
    ship_symbol with ship_size in fleet_grid was successful."""
    grid_size = len(fleet_grid)
    start_row = randint(0, grid_size - 1)
    start_col = randint(0, grid_size - 1)
    ends = get_end_indexes(start_row, start_col, ship_size)
    end_row = ends[0]
    end_col = ends[1]
    if valid_cell_indexes(start_row, start_col, grid_size) \
       and valid_cell_indexes(end_row, end_col, grid_size) \
       and not is_occupied(start_row, start_col, end_row, end_col, fleet_grid):
        place_ship(start_row, start_col, end_row, end_col,
                   fleet_grid, ship_symbol)
        return True
    return False



def generate_fleet_grid(grid_size: int, ship_symbols: list[str],
                        ship_sizes: list[int]) -> list[list[str]]:
    """Return a new grid_size by grid_size fleet grid using the ship symbols
    in ship_symbols and the corresponding ship sizes in ship_sizes."""
    fleet_grid = make_empty_fleet_grid(grid_size)

    for index in range(len(ship_symbols) - 1, -1, -1):
        ship = ship_symbols[index]
        ship_size = ship_sizes[index]
        placed = False
        while not placed:
            placed = randomly_place_ship(fleet_grid, ship, ship_size)

    return fleet_grid


def make_computer_guess(target_grid: list[list[str]]) -> list[int]:
    """Return row and column indexes for a randomly chosen UNKNOWN cell in the
    target_grid to use as the computer's next guess."""
    grid_size = len(target_grid)
    row = randint(0, grid_size - 1)
    col = randint(0, grid_size - 1)
    while target_grid[row][col] != UNKNOWN:
        row = randint(0, grid_size - 1)
        col = randint(0, grid_size - 1)
    return [row, col]


def display_grid(grid: list[list[str]]) -> None:
    """Print grid, a list of lists representing a grid, with each list on a
    new line."""
    for row in grid:
        print(' '.join(row))


def human_player_move(target_grid: list[list[str]]) -> tuple[int, int]:
    """Return the row and column indexes for the human player's guess on
    the target_grid."""
    grid_size = len(target_grid)
    print('Enter your guess in the format row,col (e.g., 1,2)')
    guess = input('> ')
    guess_parts = guess.split(',')
    row = int(guess_parts[0]) - 1
    col = int(guess_parts[1]) - 1
    while not valid_cell_indexes(row, col, grid_size) \
          or target_grid[row][col] != UNKNOWN:
        print('Please enter a valid guess in the format row,col')
        guess = input('> ')
        guess_parts = guess.split(',')
        row = int(guess_parts[0]) - 1
        col = int(guess_parts[1]) - 1
    return [row, col]



def computer_player_move(target_grid: list[list[str]]) -> tuple[int, int]:
    """Return the row and column indexes for the computer player's guess on
    the target_grid."""
    return make_computer_guess(target_grid)


def process_player_move(row: int, col: int, target_grid: list[list[str]],
                        fleet_grid: list[list[str]]) -> None:
    """Update target_grid to account for the player's guess at position
    (row, col) based on the corresponding cell in fleet_grid."""
    if fleet_grid[row][col] == EMPTY:
        target_grid[row][col] = MISS
    else:
        target_grid[row][col] = HIT



def get_ship_symbols(ship_sizes: list[int]) -> list[str]:
    """Return a list of uppercase letters of length len(ship_sizes) starting
    with 'A'."""
    symbols = []
    current_symbol = 'A'
    for _ in ship_sizes:
        symbols.append(current_symbol)
        current_symbol = chr(ord(current_symbol) + 1)
    return symbols



def play_game(grid_size: int, ship_sizes: list[int]) -> None:
    """Play a game of Battleship until the player or computer wins."""
    ship_symbols = get_ship_symbols(ship_sizes)

    # Create the fleet grid for the human player
    human_fleet_grid = generate_fleet_grid(grid_size, ship_symbols, ship_sizes)

    # Create the fleet grid for the computer player
    computer_fleet_grid = generate_fleet_grid(grid_size, ship_symbols, ship_sizes)

    # Create the target grid for the human player
    human_target_grid = make_empty_fleet_grid(grid_size)

    # Create the target grid for the computer player
    computer_target_grid = make_empty_fleet_grid(grid_size)

    player_turn = True

    while True:
        if player_turn:
            print("Your target grid:")
            display_grid(human_target_grid)
            print("Your fleet grid:")
            display_grid(human_fleet_grid)
            print("Opponent's target grid:")
            display_grid(computer_target_grid)
            print("Opponent's fleet grid:")
            display_grid(computer_fleet_grid)

            print("Your turn!")
            move = human_player_move(computer_fleet_grid)
            process_player_move(move[0], move[1], computer_target_grid,
                                computer_fleet_grid)

            if is_win(ship_sizes, human_target_grid):
                print("You win!")
                break
        else:
            print("Your target grid:")
            display_grid(human_target_grid)
            print("Your fleet grid:")
            display_grid(human_fleet_grid)
            print("Opponent's target grid:")
            display_grid(computer_target_grid)
            print("Opponent's fleet grid:")
            display_grid(computer_fleet_grid)

            print("Opponent's turn!")
            move = computer_player_move(human_fleet_grid)
            process_player_move(move[0], move[1], human_target_grid,
                                human_fleet_grid)

            if is_win(ship_sizes, computer_target_grid):
                print("Opponent wins!")
                break

        player_turn = not player_turn


if __name__ == '__main__':
    grid_size = 5
    ship_sizes = [2, 3]
    play_game(grid_size, ship_sizes)

