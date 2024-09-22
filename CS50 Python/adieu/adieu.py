import inflect

p = inflect.engine()

list = []
saying = "Adieu, adieu, to"

while True:

    try:
        Input = input("Name: ")
        print()
        list.append(Input)

    except EOFError:
        print()
        break
product = p.join(list)
print(saying,product)