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
