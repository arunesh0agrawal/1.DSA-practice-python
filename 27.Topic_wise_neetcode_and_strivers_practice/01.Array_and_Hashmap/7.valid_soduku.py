# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 



def isValidSudoku(board):
    # Check each row
    for row in board:
        if not is_valid_unit(row):
            return False

    # Check each column
    for col in zip(*board):
        if not is_valid_unit(col):
            return False

    # Check each 3x3 sub-box
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_unit(sub_box):
                return False

    return True

def is_valid_unit(unit):
    seen = set()
    for num in unit:
        if num != ".":
            if num in seen:
                return False
            seen.add(num)
    return True

# Example usage:
sudoku_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

result = isValidSudoku(sudoku_board)
print(result)  # Output: True
