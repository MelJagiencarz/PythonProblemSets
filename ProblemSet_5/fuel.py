def main():
    fraction = input('Fuel fraction: ')
    fuel = gauge(convert(fraction))
    print(f'Fuel percentange is {fuel}')


def convert(fraction):
    X, Y = map(int, fraction.split('/'))

    if Y == 0:
        raise ZeroDivisionError
    if X > Y:
        raise ValueError

    return round((X / Y) * 100)

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
