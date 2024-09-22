import sys
import csv

def main():
    cmd_line()
    list = []
    try:
        with open(sys.argv[1],"r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                split_names = row["name"].split(",")
                list.append({'name': split_names[1].lstrip(), "last": split_names[0], "house": row["house"]})


    except FileNotFoundError:
        sys.exit(f"File {sys.argv[1]} could not be read")


    with open(sys.argv[2],"w") as written_file:
        write = csv.DictWriter(written_file, fieldnames=['name','last','house'])
        write.writerow({"name":"first", "last": "last", "house": "house"})
        for row in list:
            write.writerow({"name": row["name"], "last": row["last"], "house": row['house']})

def cmd_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")



if __name__ == "__main__":
    main()
