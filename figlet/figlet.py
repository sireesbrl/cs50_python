from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font = choice(fonts))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    if not sys.argv[2] in fonts:
        print("Invalid usage")
        sys.exit(1)
    else:
        figlet.setFont(font = sys.argv[2])
else:
    print("Invalid usage")
    sys.exit(1)

text = input("Input: ").strip()
print(figlet.renderText(text))
