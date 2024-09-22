
def main():
    asdf = input("Fraction: ")
    asdf_convert = convert(asdf)
    out = gauge(asdf_convert)
    print(out)

def convert(fraction):
   while True:
    try:
        num , den = fraction.split("/")
        num = int(num)
        den = int(den)

        frac = num/den
        if frac <= 1:
            new = int (frac*100)
            return new
        else:
            asdf = input("Fraction: ")
    except ValueError:
        raise
    except ZeroDivisionError:
        raise

def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()