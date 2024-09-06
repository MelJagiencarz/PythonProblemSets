def main():
    total = 0.0
    menu = {
            "Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
            }
    while True:
        try:
            item = input('Item: ').strip().title()
            if item in menu:
                total += menu[item]
                print(f"${total:.2f}")
        except EOFError:
            print()
            break
        except KeyError:
            print('Invalid item, please enter one in the menu.')

if __name__ == "__main__":
    main()

