import sys
from PIL import Image, ImageOps

def main():
    try:
        if len(sys.argv) > 3 or len(sys.argv) < 3:
            raise FileNotFoundError
        if '.' not in sys.argv[1] or '.' not in sys.argv[2]:
            raise FileNotFoundError
        file, extention1 = sys.argv[1].split('.')
        file, extention2 = sys.argv[2].split('.')
        if extention1 != extention2:
            raise FileNotFoundError
        lis = ['jpg', 'png', 'jpeg']
        if extention1 not in lis or extention2 not in lis:
            raise FileNotFoundError

        input_path = sys.argv[1]
        output_path = sys.argv[2]
        input_image = Image.open(input_path)
        shirt_image = Image.open("shirt.png")

        fitted_image = ImageOps.fit(input_image, shirt_image.size)
        fitted_image.paste(shirt_image, (0, 0), shirt_image)
        fitted_image.save(output_path)

    except FileNotFoundError:
        if len(sys.argv) > 3:
            sys.exit('Too many command-line arguments')
        if len(sys.argv) < 3:
            sys.exit('Too few command-line arguments')
        if extention1 != extention2:
            sys.exit('Input and output have different extentions.')
        if extention1 not in lis or extention2 not in lis:
            sys.exit('Invalid format')
        sys.exit('Invalid file.')

if __name__ == "__main__":
    main()
