def main():
    greeting = input("Input: ")
    money_given = value(greeting)
    print(money_given)


def value(greeting):
    new_greeting =greeting.lower().strip()
    if new_greeting[0:5] == 'hello':
        return ("$0")

    elif new_greeting[0] =='h':
        return ("$20")

    else:
        return ("$100")


if __name__ == "__main__":
    main()