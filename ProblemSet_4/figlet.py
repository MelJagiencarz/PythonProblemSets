import sys
from pyfiglet import Figlet
from random import choice
figlet = Figlet()
fonts = figlet.getFonts()

try:
    sys.argv[1]
    sys.argv[2]
    if sys.argv[1] != '-f' or sys.argv[2] not in fonts:
        sys.exit("Invalid usage.")

    text = input('Input: ').strip()
    font = sys.argv[2]
    figlet.setFont(font=font)
    print(figlet.renderText(text))

except IndexError:
    text = input('Input: ').strip()
    font = choice(fonts)
    figlet.setFont(font=font)
    print(figlet.renderText(text))
