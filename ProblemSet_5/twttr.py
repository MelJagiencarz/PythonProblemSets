def main():
    word = input('Input: ')
    word = shorten(word)
    print(word)


def shorten(word):
    vocals = ['a', 'e', 'i', 'o', 'u']
    output = ''

    for char in word:
        if char.lower() in vocals:
            continue
        output += char

    return output


if __name__ == "__main__":
    main()
