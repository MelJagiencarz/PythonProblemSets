import datetime
import sys
import operator
import inflect

def main():
    print(convert(input("Your birth date: ")))


def convert(s):
    try:
        date_object = datetime.datetime.strptime(s, '%Y-%m-%d').date()
        result_days = operator.sub(datetime.date.today(), date_object)
        result_mins = result_days.days * 24 * 60
        p = inflect.engine()
        return f'{p.number_to_words(result_mins, andword="").capitalize()} minutes'

    except ValueError:
        sys.exit('Invalid date format.')

if __name__ == "__main__":
    main()
