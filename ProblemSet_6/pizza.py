import tabulate
import sys
import csv

try:
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    file, extention = sys.argv[1].split('.')
    if extention != 'csv':
        sys.exit('Not a CSV file')

    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        print(tabulate.tabulate(reader, headers="firstrow", tablefmt="grid"))

except FileNotFoundError:
    sys.exit('File does not exist')
