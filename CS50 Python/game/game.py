import random

while True:
    try:
        num = int(input("Level: "))
        if num >= 1:
            break

    except:
        pass


answer = random.randint(1,10)

while True:
    try:
        guess = int(input("Guess: "))
        if guess == answer:
            print("Just right!")
            break
        elif guess < answer:
            print("Too small!")
            pass
        else:
            print("Too large!")
            pass


    except:
        pass