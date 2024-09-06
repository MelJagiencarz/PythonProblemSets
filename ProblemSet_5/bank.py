def main():
    greeting = input("Greeting: ")
    greeting = value(greeting)
    print(greeting)

def value(greeting):
    if "Hello" in greeting:
        return 0
    elif "H" in greeting:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
