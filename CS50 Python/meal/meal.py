def main():
    clock = input("What time is it currently:")
    time = convert(clock)
    if 7 <= time <= 8:
        print('Breakfast time')
    elif 12 <= time <= 13:
        print('Lunch time')
    elif 18 <= time <= 19:
        print('Dinner time')


def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute)
    minute = minute/60
    return hour + minute

if __name__ == "__main__":
    main()