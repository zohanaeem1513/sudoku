from pprint import pprint

EMPTY = -1


def find_next_empty(puzzle: list[list[int]]) -> tuple[int | None, int | None]:
    """
    Find the next empty cell in the Sudoku board.
    Returns (row, col) or (None, None) if the board is full.
    """
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == EMPTY:
                return row, col

    return None, None


def is_valid(puzzle: list[list[int]], guess: int, row: int, col: int) -> bool:
    """
    Check whether placing 'guess' at (row, col) follows Sudoku rules.
    """

    # Check row
    if guess in puzzle[row]:
        return False

    # Check column
    if guess in [puzzle[r][col] for r in range(9)]:
        return False

    # Check 3x3 box
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True


def solve_sudoku(puzzle: list[list[int]]) -> bool:
    """
    Solve the Sudoku puzzle using backtracking.
    Returns True if a solution exists.
    """

    # Find an empty cell
    row, col = find_next_empty(puzzle)

    # No empty cells left → puzzle solved
    if row is None:
        return True

    # Try every possible number
    for guess in range(1, 10):

        if is_valid(puzzle, guess, row, col):

            # Place the guess
            puzzle[row][col] = guess

            # Recursively solve the rest
            if solve_sudoku(puzzle):
                return True

            # Backtrack
            puzzle[row][col] = EMPTY

    # No valid number found
    return False


if __name__ == "__main__":

    example_board = [
        [3, 9, EMPTY, EMPTY, 5, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, 2, EMPTY, EMPTY, EMPTY, EMPTY, 5],
        [EMPTY, EMPTY, EMPTY, 7, 1, 9, EMPTY, 8, EMPTY],

        [EMPTY, 5, EMPTY, EMPTY, 6, 8, EMPTY, EMPTY, EMPTY],
        [2, EMPTY, 6, EMPTY, EMPTY, 3, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, 4],

        [5, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [6, 7, EMPTY, 1, EMPTY, 5, EMPTY, 4, EMPTY],
        [1, EMPTY, 9, EMPTY, EMPTY, EMPTY, 2, EMPTY, EMPTY],
    ]

    solved = solve_sudoku(example_board)

    print("Solved:", solved)
    pprint(example_board)
