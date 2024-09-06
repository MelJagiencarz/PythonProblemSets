def convert():
    face_text = input()

    face_text = face_text.replace(':)', '🙂')
    face_text = face_text.replace(':(', '🙁')
    face_text = face_text.replace(':) :(', '🙂 🙁')

    return face_text  # Add a return statement to return the modified text

def main():
    print(convert())


main()
