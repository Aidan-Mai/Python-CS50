import pyfiglet
from pyfiglet import Figlet
import sys,random

if len(sys.argv) == 1:
    randomFont = True
elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] =="--font":
    randomFont = False
else:
    sys.exit(1)





figlet = Figlet()
figlet.getFonts()

if randomFont == True:
    font = random.choice(figlet.getFonts())
elif randomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)


text = input("Input: ")
print(figlet.renderText(text))