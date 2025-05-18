import numpy as np
from sudoku import Sudoku
from window import SudokuVisualizer


FILE_PATH = 'example.csv'


def check_if_original(index: list, sudoku_original: np.ndarray) -> bool:
    '''Check if the index is in the original sudoku matrix'''
    if sudoku_original[index[0]][index[1]] != 0:
        return True
    else:
        return False

def index_increment(index) -> list:
    '''Increment the index by one'''

    # If the index x cordinate is one the last spot, change row
    if index[0] == 8:
        index = [0, index[1]+1]
    else:
        index[0] += 1
    return index

def index_decrement(index) -> list:
    '''Decrement the index by one'''

    # If the index x cordinate is one the last spot, change row
    if index[0] == 0:
        index = [8, index[1]-1]
    else:
        index[0] -= 1
    return index

def check_outofbound(index) -> bool:
    '''Return True if the index is out of bounds'''

    if (index[0] not in range(9)) or \
       (index[1] not in range(9)):
        return True

    else:
        return False

def main() -> None:

    # Create the sudoku
    sudoku = Sudoku()
    window = SudokuVisualizer()


    # Chack for the arguments
    if FILE_PATH:
        sudoku.import_from_file(FILE_PATH)


    index = [0,0]
    solved = False
    while not solved:

        # Visualize the sudoku solver
        window.draw_grid()
        window.draw_numbers(sudoku.current, sudoku.original)
        window.flip()


        # Check if the index is inside the original sudoku
        if check_if_original(index, sudoku.original):

            index = index_increment(index)

            # If True then the index is on the last cell and its an original number
            solved = check_outofbound(index)

            continue

        # Update attempt
        result = sudoku.increment_attempt(index)

        # If the result is negative than rollback the index
        if not result:
            sudoku.zero_attempt(index)
            # Rollback the index until it hits a value that is not in the original
            while True:
                index = index_decrement(index)
                if not check_if_original(index, sudoku.original):
                    break
            continue
        
        # Check if the current configuration is valid
        result = sudoku.check9x9()

        # If the grid is valid step to the next cell, otherwise repeat
        if result:
            index = index_increment(index)
        else:
            continue
        
        # Check if the sudoku is solved
        solved = check_outofbound(index)
        
    print(sudoku.current)


if __name__ == '__main__':
    main()