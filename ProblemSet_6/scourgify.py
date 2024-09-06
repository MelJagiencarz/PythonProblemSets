import csv
import sys

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        with open(input_filename, mode='r', newline='') as infile:
            reader = csv.DictReader(infile)
            with open(output_filename, mode='w', newline='') as outfile:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    last_name, first_name = row['name'].split(", ")
                    writer.writerow({'first': first_name, 'last': last_name, 'house': row['house']})

    except FileNotFoundError:
        sys.exit(f"Could not read {input_filename}")

if __name__ == "__main__":
    main()
