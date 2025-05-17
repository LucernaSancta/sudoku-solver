import sys
from sudoku import Sudoku

# Create arguments dictionary
args_dict = {
    '-i': False
}


args = sys.argv[1:]
# Read every argument
while args:

    match args[0]:

        # Import argument
        case '-i':
            try:
                args_dict['-i'] = args[1]
                args.pop(1)
            except IndexError:
                print('The -i flag must be followed by a file path')
            
    args.pop(0)


# Create the sudoku
sudoku = Sudoku()


# Chack for the arguments
if args_dict['-i']:
    sudoku.import_from_file(args_dict['-i'])


sudoku.print_current()