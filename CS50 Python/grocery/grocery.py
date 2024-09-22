list = {

}


while True:
    try:
        name = input("").upper()
        if name in list:
            list[name] += 1
        else:
            list[name] = 1
    except  EOFError:
        print()
        for item in sorted(list.keys()):
            print(list[item], item )

        break
