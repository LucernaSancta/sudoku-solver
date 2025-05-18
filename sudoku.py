import csv
import numpy as np


class Sudoku:
    def __init__(self):

        # Get 9x9 grid of 0's to represent empty cells
        self._original = np.zeros(shape=(9,9), dtype=int)
        self._attempt = np.zeros(shape=(9,9), dtype=int)
    
    def create_sudoku(self, values: list = []) -> None:
        
        if type(values[0][0]) is int:
            self._original = np.array(values)

        elif type(values[0][0]) is str:
            self._original = np.array(values) # Create numpy array
            self._original[self._original == ' '] = '0' # Change all the spaces with 0's
            self._original = self._original.astype(int) # Transform array from str to int

    def import_from_file(self, file_path: str) -> None:

        # Open the csv file
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')

            self.create_sudoku(list(spamreader))
    
    @property
    def current(self) -> np.array:
        return self._original
    
    def check9x1(self, value: np.ndarray) -> bool:
        '''
        Check if an array like object is valid, returns False if not.
        To be valid:
         - all values need to be unique (exept for 0's)
         - all elemetns need to be between 1 and 9
         - the sum must be 45 or less (9+8+7+6+5+4+3+2+1)
        '''

        value = value[value != 0] # Remove all the 0's

        # Check if all values are unique
        if len(value) != len(np.unique(value)):
            return False

        # check if array values lie in the range [1, 9]
        if not ((value >= 1) & (value <= 9)).all():
            return False
        
        # Check if the sum is less than 45
        if sum(value) > 45:
            return False

        # The array is valid
        return True


if __name__ == '__main__':
    sudoku = Sudoku()
    sudoku.import_from_file('example.csv')