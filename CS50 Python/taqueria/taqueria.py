
foods = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

price = 0

while True:
    try:
        name = input("Item: ").title()
        if name in foods:
            price += foods[name]
            print("$", end="")
            print("{:.2f}".format(price))

    except  EOFError:
        print()
        break
