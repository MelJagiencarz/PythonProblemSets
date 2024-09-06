def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if any(char in ' .-' for char in s):
        return False

    if not s[:2].isalpha():
        return False

    digit_started = False
    for char in s:
        if char.isdigit():
            digit_started = True
        elif digit_started:
            return False

    return True


main()
