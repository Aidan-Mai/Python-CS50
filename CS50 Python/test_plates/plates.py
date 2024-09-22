def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) <2 or len(s) > 6:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1

    i = 0
    temp = ""
    checker = False
    while i < len(s):
        temp = s[i]

        if temp.isdigit():
            checker = True

        if checker:
            if not temp.isdigit():
                return False
        i += 1


    for char in s:
        if char in ['.',' ', '!', '?']:
            return False



    return True
if __name__ == "__main__":
    main()