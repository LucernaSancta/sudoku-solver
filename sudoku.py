import csv
import numpy as np


class Sudoku:
    def __init__(self):

        self.create_sudoku()
    
    def create_sudoku(self, values: list = []) -> None:
        '''
        Create the numpy values from a list of existing values,
        create a new one if no value is provided
        '''

        if not values:
            # Get 9x9 grid of 0's to represent empty cells
            self.values = np.zeros(shape=(9,9), dtype=int)
            return
        
        elif type(values[0][0]) is int:
            self.values = np.array(values)

        elif type(values[0][0]) is str:
            self.values = np.array(values) # Create numpy array
            self.values[self.values == ' '] = '0' # Change all the spaces with 0's
            self.values = self.values.astype(np.int8) # Transform array from str to int

    def import_from_file(self, file_path: str) -> None:

        # Open the csv file
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')

            self.create_sudoku(list(spamreader))
    
    def print_current(self) -> None:
        print(self.values)
    
    def check(self) -> bool:
        '''Chack if the current configuration is valid, returns False if not'''
        pass


if __name__ == '__main__':
    sudoku = Sudoku()
    sudoku.import_from_file('example.csv')
    sudoku.print_current()