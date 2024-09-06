import random


def main():
    correct = 0
    level = get_level()

    for problem in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        result = X + Y
        errors = 0

        while errors < 3:
            answer = input(f'{X} + {Y} = ').strip()
            if int(answer) == result:
                correct += 1
                break
            else:
                print('EEE')
                errors += 1

        if errors == 3:
            print(result)
    print(f'{correct}')

def get_level():
    while True:
        try:
            level = int(input('Level: ').strip())
            if level in [1, 2, 3]:
                return level
            else:
                raise ValueError
        except ValueError:
            print('Invalid level, please insert a valid one.')


def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
