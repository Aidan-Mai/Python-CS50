import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.search(r"^(([0-9][0-2]*):?([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):?([0-5][0-9])*) ([A-P]M)$", s):
        split = time.groups()
        if int(split[1]) > 12 or int(split[5]) > 12:
            raise ValueError
        first = correct(split[1], split[2], split[3])
        second = correct(split[5], split[6], split[7])
        return (first +" to "+ second)

    else:
        raise ValueError


def correct(hour,min,ampm):
    if ampm == "PM":
        if int(hour) == 12:
            n_hour = 12
        else:
            n_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            n_hour = 0
        else:
            n_hour = int(hour)
    if min == None:
        n_min = ":00"
        correct_time = f"{n_hour:02}" + n_min
    else:
        n_min = min
        correct_time = f"{n_hour:02}"  + ":" + n_min
    return correct_time
...


if __name__ == "__main__":
    main()

