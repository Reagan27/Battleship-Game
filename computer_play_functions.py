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
    while is_not_given_symbol(row, col, target_grid, UNKNOWN):
        row = randint(0, grid_size - 1)
        col = randint(0, grid_size - 1)
    return [row, col]


if __name__ == '__main__':
    #run doctest
    import doctest
    doctest.testmod()
