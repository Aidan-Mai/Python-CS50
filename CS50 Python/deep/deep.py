number = str(input("Type here --> :"))

number = number.lower()
number = number.strip()
match number:
    case "42":
        print("Yes")
    case "forty-two":
        print("Yes")
    case "forty two":
        print("Yes")
    case _:
        print("No")