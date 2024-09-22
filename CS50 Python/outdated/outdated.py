months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"

]


while True:
    date = input("Date: ")
    try:
        month,day,year = date.split("/")
        if 1<= int(month) <=12 and 1<= int(day) <=31:
            break
    except:
        try:
            space_month,space_day,year = date.split(" ")
            if "," in space_day:
                for m in range(len(months)):
                    if space_month == months[m]:
                        month = m + 1

            day = space_day.replace(",", "")
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                break
        except:
            print()
            pass


print(f"{int(year)}-{int(month):02}-{int(day):02}")