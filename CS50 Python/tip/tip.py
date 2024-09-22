def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar_sign = d.replace('$',"")
    return float(dollar_sign)

def percent_to_float(p):
    percent_sign = p.replace("%","")
    convert = float(percent_sign) / 100
    return (convert)


main()