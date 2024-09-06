def main():
    while True:
        try:
            fuel = input('Fraction: ')
            X, Y = fuel.split('/')
            X = int(X)
            Y = int(Y)

            if X > Y or Y == 0:
                raise ValueError

            percentage = (X / Y) * 100

            if percentage <= 1:
                tank = 'E'
            elif percentage >= 99:
                tank = 'F'
            elif 25 - 1 <= percentage <= 25 + 1:
                tank = '25%'
            elif 50 - 1 <= percentage <= 50 + 1:
                tank = '50%'
            elif 75 - 1 <= percentage <= 75 + 1:
                tank = '75%'
            else:
                tank = f'{percentage:.0f}%'

            print(tank)
            break

        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction.")

if __name__ == "__main__":
    main()
