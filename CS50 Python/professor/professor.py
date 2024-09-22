import random


def main():
    level = get_level()
    score = games(level)
    print(score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

def rounds(x,y):
    r = 0
    while r != 3:
        try:
            ans = int(input(f"{x} + {y} = "))
            if ans == (x + y):
                return True
            else:
                print("EEE")
                r += 1

        except:
            r += 1
            print('EEE')
    print(f"{x} + {y} = {x+y}")
    return False
def games(level):
    count = 1
    score = 0
    while count <= 10:
        x,y = generate_integer(level)
        equation = rounds(x,y)
        if equation == True:
            score += 1
        count += 1
    return score
if __name__ == "__main__":
    main()