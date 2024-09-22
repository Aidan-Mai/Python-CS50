import sys
from os.path import splitext
from PIL import Image, ImageOps
def main():
    cmd_line()
    try:
        picture = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    resize = ImageOps.fit(picture,size)
    resize.paste(shirt,shirt)
    resize.save(sys.argv[2])

def cmd_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    one = splitext(sys.argv[1])
    two = splitext(sys.argv[2])

    if (checker(one[1])) == False:
        sys.exit("invalid Input")
    if checker(two[1]) == False:
        sys.exit("invalid Output")
    if one[1].lower() != two[1].lower():
        sys.exit("Input and Output have different extensions")
def checker(file):
    if file in [".jpg",".png","jpeg"]:
        return True
    return False

if __name__ == "__main__":
    main()
