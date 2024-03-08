import os
from typing import TextIO
from battleship_game_functions import MIN_SHIP_SIZE, MAX_SHIP_SIZE, \
                                      MAX_GRID_SIZE, UNKNOWN, EMPTY, HIT, MISS
from battleship_game_functions import valid_cell_indexes, \
                                      is_not_given_symbol, is_win, \
                                      update_target_grid, update_fleet_grid, \
                                      validate_symbol_counts, \
                                      validate_ship_positions
from computer_play_functions import generate_fleet_grid, make_computer_guess

HIT_MESSAGE = 'hit a ship'
MISS_MESSAGE = 'missed'

def read_game_file() -> list[list]:
    """Return the ship and symbol grid data from a game file whose file name
    was provided by the game user.
    
    The first item in the returned nested list is a list[str] (ship symbols).
    The second item in the returned nested list is a list[int] (the sizes of
      the corresponding ships in the first item.
    The third item in the returned nested list is a list[list[str]] (the
      player's fleet grid placements).
    """
    filename = get_valid_filename('\nEnter the name of a game file: ')
    with open(filename) as game_file:
        ships_data = read_ship_data(game_file)
        ship_symbols = ships_data[0]
        ship_sizes = ships_data[1]
        fleet_grid = read_fleet_grid(game_file)
    return [ship_symbols, ship_sizes, fleet_grid]


def get_valid_filename(msg: str) -> str:
    """Return the name of a file entered by the user when prompted with msg.
    A file with the entered file name should exist in the same folder as
    this file. Keep prompting the user until a valid file name is entered.
    """
    filename = input(msg)
    while not os.path.exists(filename):
        print('That file does not exist in this folder. Please try again.')
        filename = input(msg)
    return filename


def read_ship_data(game_file: TextIO) -> list[list]:
    """Return a list containing the ship symbols in game_file as a list of
    strings at index 0, and the ship sizes in game_file as a list of ints at
    index 1.
    """
    ship_symbols = game_file.readline().strip().split()
    ship_sizes = [int(size) for size in game_file.readline().strip().split()]
    return [ship_symbols, ship_sizes]


def read_fleet_grid(game_file: TextIO) -> list[list[str]]:
    """Return the fleet grid that is found in game_file."""
    fleet_grid = []
    for line in game_file:
        fleet_grid.append(list(line.strip()))
    return fleet_grid


def is_valid_game(fleet_grid: list[list[str]], ship_symbols: list[str],
                  ship_sizes: list[int]) -> bool:
    """Return True if and only if the game parameters fleet_grid, ship_symbols,
    and ship_sizes are valid, and fleet_grid is a valid grid.
    """
    return validate_game_parameters(fleet_grid, ship_symbols, ship_sizes) \
           and validate_fleet_grid(fleet_grid, ship_symbols, ship_sizes)


def validate_game_parameters(fleet_grid: list[list[str]],
                             ship_symbols: list[str],
                             ship_sizes: list[int]) -> bool:
    """Return True if and only if fleet_grid is square with at least one cell
    and at most MAX_GRID_SIZE cells per row, the number of ship symbols in
    ship_symbols is the same as the number of sizes in ship_sizes, that there
    is at least one ship, all ships have a valid size, and all ships have a
    valid, unique character label.
    """
    if len(fleet_grid) == 0 or len(fleet_grid) > MAX_GRID_SIZE:
        return False
    for row in fleet_grid:
        if len(row) != len(fleet_grid):
            return False
    if len(ship_symbols) != len(ship_sizes) or len(ship_symbols) == 0:
        return False
    for size in ship_sizes:
        if size < MIN_SHIP_SIZE or size > MAX_SHIP_SIZE:
            return False
    for ship_symbol in ship_symbols:
        if len(ship_symbol) != 1:
            return False
    for i in range(len(ship_symbols)):
        for j in range(len(ship_symbols)):
            if i != j and ship_symbols[i] == ship_symbols[j]:
                return False
    return True


def validate_fleet_grid(fleet_grid: list[list[str]],
                        ship_symbols: list[str],
                        ship_sizes: list[int]) -> bool:
    """Return True if and only if fleet_grid contains a ship of the correct
    size for each ship in ship_symbols and with the corresponding size from
    ship_sizes, and nothing else except for the EMPTY character. Each ship in
    ship_symbols must also have a valid alignment (all symbols appearing across
    a row or down a column) in fleet_grid.
    """
    return validate_symbol_counts(fleet_grid, ship_symbols, ship_sizes) \
           and validate_ship_positions(fleet_grid, ship_symbols, ship_sizes)


def get_target_grid(grid_size: int) -> list[list[str]]:
    """Return a grid_size by grid_size grid of UNKNOWN characters."""
    return [[UNKNOWN] * grid_size for _ in range(grid_size)]


def display_grids(target_grid: list[list[str]],
                  fleet_grid: list[list[str]]) -> None:
    """Display the target_grid and the fleet_grid that belong to a player."""
    print('\nMy target grid.               My fleet grid.\n')
    gap_between_grids = ' ' * (28 - len(target_grid))

    # Display the column numbers
    print(' ', end='')
    for col in range(len(target_grid)):
        print(col, end='')
    print(gap_between_grids + ' ', end='')
    for col in range(len(target_grid)):
        print(col, end='')
    print()

    # Display row numbers and cell contents.
    for row in range(len(target_grid)):
        print(row, end='')
        for col in range(len(target_grid)):
            print(target_grid[row][col], end='')
        print(gap_between_grids + str(row), end='')
        for col in range(len(fleet_grid)):
            print(fleet_grid[row][col], end='')
        print()

    print()
    print(' ' + HIT + ' means hit,                Upper-case means hit.')
    print(' ' + MISS + ' means miss.')


def get_row_col() -> list[int]:
    """Return the row and column indexes entered by the user when prompted."""
    row = input('Please enter the row: ')
    col = input('Please enter the column: ')
    if row.isdigit() and col.isdigit():
        row = int(row)
        col = int(col)
    else:
        row = -1
        col = -1
    return [row, col]


def get_valid_player_move(target_grid: list[list[str]]) -> list[int]:
    """Return a two-item list that contains the player's move."""
    grid_size = len(target_grid)
    [row, col] = get_row_col()
    while (not valid_cell_indexes(row, col, grid_size) or
           is_not_given_symbol(row, col, target_grid, UNKNOWN)):
        print('Invalid move! Either already known or invalid indexes! \n')
        [row, col] = get_row_col()
    return [row, col]


def make_move(row: int, col: int, fleet_grid: list[list[str]],
              ship_symbols: list[str], hits_list: list[int],
              target_grid: list[list[str]]) -> str:
    """Return HIT_MESSAGE and update hits_list and fleet_grid, using
    ship_symbols, if there is a ship at row and col, or return MISS_MESSAGE if
    there is no ship at row and col. Update target_grid in both cases.
    """
    if is_not_given_symbol(row, col, fleet_grid, EMPTY):
        update_fleet_grid(row, col, fleet_grid, ship_symbols, hits_list)
        update_target_grid(row, col, target_grid, fleet_grid)
        return HIT_MESSAGE
    else:
        update_target_grid(row, col, target_grid, fleet_grid)
        return MISS_MESSAGE


def get_num_moves(target_grid: list[list[str]]) -> int:
    """Return the number of moves made so far for the board target_grid."""
    moves_count = 0
    for row in target_grid:
        for symbol in row:
            if symbol != UNKNOWN:
                moves_count += 1
    return moves_count


def play_single_player() -> None:
    """A single-player game with no opponent."""
    ship_symbols, ship_sizes, fleet_grid = read_game_file()
    if not is_valid_game(fleet_grid, ship_symbols, ship_sizes):
        print('The supplied game is not valid. Game exiting.')
        return

    target_grid = get_target_grid(len(fleet_grid))
    display_grids(target_grid, fleet_grid)
    hits_list = [0] * len(ship_sizes)

    while not is_win(ship_sizes, hits_list):
        print('\nTake a turn.')
        [row, col] = get_valid_player_move(target_grid)
        print()

        message = make_move(row, col, fleet_grid, ship_symbols,
                            hits_list, target_grid)
        print(f'You {message}!')

        if is_not_given_symbol(row, col, fleet_grid, EMPTY):
            ship_index = ship_symbols.index(fleet_grid[row][col].lower())
            if hits_list[ship_index] >= ship_sizes[ship_index]:
                ship_size = ship_sizes[ship_index]
                ship_symbol = ship_symbols[ship_index]
                print(f'The size {ship_size} {ship_symbol} ship ' \
                       'has been sunk!')

        display_grids(target_grid, fleet_grid)

    print(f'\nYou won in {get_num_moves(target_grid)} move(s)!')
    

if __name__ == '__main__':
    play_single_player()
