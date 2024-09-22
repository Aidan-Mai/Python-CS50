from datetime import datetime,date
import inflect

p = inflect.engine()

class Date:
    def __init__(self,start_time,end_time):
        self.start = start_time
        self.end = end_time

    def Calculation(self):

        #subtracts the beginning and start of the time
        difference = self.end - self.start

        self.minutes = int(difference.total_seconds() / 60)
        self.msg =  (p.number_to_words(self.minutes, andword=""))



        return self.msg.capitalize()






def twodates():
    start = datetime.today().strftime('%Y-%m-%d')
    end =(input("Enter the end date YYYY-MM-D: "))
    try:
        start_time =(datetime.strptime(start, "%Y-%m-%d"))
        end_time = (datetime.strptime(end, "%Y-%m-%d"))
    except ValueError:
        exit("invald date")
    return Date(start_time,end_time)


def main():
    test = twodates()
    print(test.Calculation())



...


if __name__ == "__main__":
    main()
