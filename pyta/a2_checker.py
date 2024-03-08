"""A simple checker for types of functions in battleship_game_functions.py"""

import checker_generic
import pytest
import battleship_game_functions as bgf
from typing import Any
# from python_helper import bound_timeout

FILENAME = 'battleship_game_functions.py'
PYTA_CONFIG = 'pyta/a2_pythonta.json'
TARGET_LEN = 79
SEP = '='

CONSTANTS = {
    'MIN_SHIP_SIZE': 1,
    'MAX_SHIP_SIZE': 10,
    'MAX_GRID_SIZE': 10,
    'EMPTY': '.',
    'UNKNOWN': '-',
    'HIT': 'X',
    'MISS': 'M'
}


def _check(func: callable, args: list, expected: type) -> tuple[bool, object]:
    """Check if a call to func(args) returns a result with type expected.

    Return (True, result-of-call) if the check succeeds.
    Return (False, error-or-failure-message) if anything goes wrong.
    """
    try:
        returned = func(*args)
    except Exception as exn:
        return False, _error_message(func, args, exn)

    if isinstance(returned, expected):
        return True, returned

    return False, _type_error_message(func, expected.__name__, returned)


def _check_nested_type(func: callable, args: list, tp: type):
    """Check if func(args) returns a list of elements of type tp.

    Return (True, result-of-call) if the check succeeds.
    Return (False, error-or-failure-message) if anything goes wrong.

    """

    success, result = _check(func, args, list)
    if not success:
        return False, result

    msg = _type_error_message(func, 'list of {}s'.format(tp.__name__), result)

    for item in result:
        if not isinstance(item, tp):
            return False, msg

    return True, result


def _type_error_message(func: callable, expected: str, got: object) -> str:
    """Return an error message for function func returning got, where the
    correct return type is expected.
    """
    return f'{func.__name__} should return a {expected}, but ' \
           f'instead it returned {got}.'


def _error_message(func: callable, args: list, error: Exception) -> str:
    """Return an error message: func(args) raised an error."""
    args = str.join(',', map(str, args))
    return f'The call {func.__name__}({args}) caused an error: {error}'


class TestChecker:
    """Sanity checker for assignment functions."""
    module = bgf

#    @bound_timeout(30)
    def test_valid_cell_indexes(self) -> None:
        """Check the type contract of function valid_cell_indexes."""
        self._check(bgf.valid_cell_indexes, [2, 9, 10], bool)

#    @bound_timeout(30)
    def test_is_not_given_symbol(self) -> None:
        """Check the type contract of function is_not_given_symbol."""
        unknown = CONSTANTS['UNKNOWN']
        f_g = [['a', unknown], [unknown, 'b']]
        f_g_copy = [['a', unknown], [unknown, 'b']]
        self._check(bgf.is_not_given_symbol, [1, 1, f_g, unknown],
                    bool)
        self._check_no_mutation(bgf.is_not_given_symbol, f_g, f_g_copy)

#    @bound_timeout(30)
    def test_is_win(self) -> None:
        """Check the type contract of function is_win."""
        list1 = [1, 2, 3]
        list1_copy = [1, 2, 3]
        list2 = [1, 2, 3]
        list2_copy = [1, 2, 3]
        self._check(bgf.is_win, [list1, list2], bool)
        self._check_no_mutation(bgf.is_win, list1, list1_copy)
        self._check_no_mutation(bgf.is_win, list2, list2_copy)

#     @bound_timeout(30)
    def test_update_target_grid(self) -> None:
        """Check the type contract of function update_target_grid."""
        unknown = CONSTANTS['UNKNOWN']
        empty = CONSTANTS['EMPTY']
        t_g = [[unknown, unknown], [unknown, unknown]]
        t_g_copy = [[unknown, unknown], [unknown, unknown]]
        f_g = [['a', 'b'], ['a', empty]]
        f_g_copy = [['a', 'b'], ['a', empty]]
        self._check(bgf.update_target_grid, [1, 1, t_g, f_g], type(None))
        self._check_mutation(bgf.update_target_grid, t_g, t_g_copy)
        self._check_no_mutation(bgf.update_target_grid, f_g, f_g_copy)

#     @bound_timeout(30)
    def test_update_fleet_grid(self) -> None:
        """Check the type contract of function update_fleet_grid."""
        empty = CONSTANTS['EMPTY']
        f_g = [[empty, 'a'], [empty, 'a']]
        f_g_copy = [[empty, 'a'], [empty, 'a']]
        ships = ['a']
        ships_copy = ['a']
        h_l = [0]
        h_l_copy = [0]
        self._check(bgf.update_fleet_grid, [0, 1, f_g, ships, h_l], type(None))
        self._check_mutation(bgf.update_fleet_grid, f_g, f_g_copy)
        self._check_no_mutation(bgf.update_fleet_grid, ships, ships_copy)
        self._check_mutation(bgf.update_fleet_grid, h_l, h_l_copy)

#     @bound_timeout(30)
    def test_get_ship_symbol_count(self) -> None:
        """Check the type contract of function get_ship_symbol_count."""
        f_g = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
        f_g_copy = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
        self._check(bgf.get_ship_symbol_count, [f_g, 'c'], int)
        self._check_no_mutation(bgf.get_ship_symbol_count, f_g, f_g_copy)

#     @bound_timeout(30)
    def test_has_ship(self) -> None:
        """Check the type contract of function has_ship."""
        empty = CONSTANTS['EMPTY']
        f_g = [[empty, 'b', empty], ['a', 'b', empty], [empty, empty, empty]]
        f_g_copy = [[empty, 'b', empty], ['a', 'b', empty],
                    [empty, empty, empty]]
        self._check(bgf.has_ship, [f_g, 0, 1, 'b', 2], bool)
        self._check_no_mutation(bgf.has_ship, f_g, f_g_copy)

#     @bound_timeout(30)
    def test_validate_symbol_counts(self) -> None:
        """Check the type contract of function validate_symbol_counts."""
        empty = CONSTANTS['EMPTY']
        f_g = [[empty, 'b', empty], [empty, 'b', empty], ['a', 'a', 'a']]
        f_g_copy = [[empty, 'b', empty], [empty, 'b', empty], ['a', 'a', 'a']]
        ships = ['a', 'b']
        ships_copy = ['a', 'b']
        sizes = [3, 2]
        sizes_copy = [3, 2]
        self._check(bgf.validate_symbol_counts, [f_g, ships, sizes], bool)
        self._check_no_mutation(bgf.validate_symbol_counts, f_g, f_g_copy)
        self._check_no_mutation(bgf.validate_symbol_counts, ships, ships_copy)
        self._check_no_mutation(bgf.validate_symbol_counts, sizes, sizes_copy)

#     @bound_timeout(30)
    def test_validate_ship_positions(self) -> None:
        """Check the type contract of function validate_ship_positions."""
        empty = CONSTANTS['EMPTY']
        f_g = [[empty, 'b', empty], [empty, 'b', empty], ['a', 'a', 'a']]
        f_g_copy = [[empty, 'b', empty], [empty, 'b', empty], ['a', 'a', 'a']]
        ships = ['a', 'b']
        ships_copy = ['a', 'b']
        sizes = [3, 2]
        sizes_copy = [3, 2]
        self._check(bgf.validate_ship_positions, [f_g, ships, sizes], bool)
        self._check_no_mutation(bgf.validate_ship_positions, f_g, f_g_copy)
        self._check_no_mutation(bgf.validate_ship_positions, ships, ships_copy)
        self._check_no_mutation(bgf.validate_ship_positions, sizes, sizes_copy)

    def _check(self, func: callable, args: list, desired_type: type,
               nested: bool = False) -> None:
        """Check that func called with arguments args returns a value of type
        ret_type. Display the progress and the result of the check.
        """
        if not nested:
            result, message = _check(func, args, desired_type)
        else:
            result, message = _check_nested_type(func, args, desired_type)

        print(message)
        assert result is True, message

    def _check_no_mutation(self, func: callable, actual, expected) -> None:
        """Check that func does not mutate the argument actual so that it still
        matches expected.
        """
        assert expected == actual, '{0} should not mutate its arguments'.format(
            func.__name__)

    def _check_mutation(self, func: callable, actual, expected) -> None:
        """Check that func mutates the argument actual so that it is different
        from expected.
        """
        assert expected != actual, '{0} should mutate its list argument'.format(
            func.__name__)

#    @bound_timeout(30)
    def test_check_constants(self) -> None:
        """Check that, for each (name, value) pair in name2value, the value of
        a variable named name in module mod is value.
        """

        for name, expected in CONSTANTS.items():
            actual = getattr(self.module, name)
            msg = 'The value of constant {} should be {} but is {}.'.format(
                name, expected, actual)
            assert expected == actual, msg


print(''.center(TARGET_LEN, SEP))
print(' Start: checking coding style with PythonTA '.center(TARGET_LEN, SEP))
checker_generic.run_pyta(FILENAME, PYTA_CONFIG)
print(' End checking coding style with PythonTA '.center(TARGET_LEN, SEP))

print(' Start: checking type contracts '.center(TARGET_LEN, SEP))
pytest.main(['--show-capture', 'no', '--disable-warnings', '--tb=short',
             'a2_checker.py'])
print(' End checking type contracts '.center(TARGET_LEN, SEP))

print('\nScroll up to see ALL RESULTS:')
print('  - checking coding style with Python TA')
print('  - checking type contract\n')
