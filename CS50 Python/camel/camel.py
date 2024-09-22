camel_Case = str(input("camel_case:"))

print("snake_case: ", end='')



for i in camel_Case:
    if i.isupper():
        print('_' + i.lower(), end='')
    else:
        print(i,end='')
print()
