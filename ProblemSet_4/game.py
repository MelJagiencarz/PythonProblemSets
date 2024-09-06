import random

while True:
    try:
        level = input('Level: ').strip()
        if int(level) < 1 or isinstance(level, int):
            raise ValueError
        result = random.randint(1, int(level))

        guess = int(input('Guess: ').strip())
        if int(guess) < 1 or isinstance(level, int):
            raise ValueError

        if int(guess) < result:
            print('Too small!')
        if int(guess) > result:
            print('Too large!')
        if int(guess) == result:
            print('Just right!')
            break


    except ValueError:
        pass
