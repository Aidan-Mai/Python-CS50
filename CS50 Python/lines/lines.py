import sys

def main():
    check_cmd_line()
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    count = 0
    for line in lines:
        if checker(line) == True:
            count += 1
    print(count)





def check_cmd_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a python file")
def checker(line):
    if line.isspace():
        return False
    if line.lstrip().startswith("#"):
        return False
    return True

if __name__ == "__main__":
    main()