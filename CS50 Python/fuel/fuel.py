while True:
    fuel = input("Fraction: ")
    try:
        num , den = fuel.split("/")
        num = int(num)
        den = int(den)

        frac = num/den
        if frac <= 1:
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass



total = round(frac * 100)

if total <= 1:
    print("E")
elif total >= 99:
    print("F")
else:
    print(f"{total}%")
