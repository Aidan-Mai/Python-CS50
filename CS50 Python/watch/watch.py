import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*></iframe>",s):
        if checker := re.search(r"(https?://(www\.)?youtube\.com/embed/(\w*))",s,re.IGNORECASE):
           new = re.sub(r"www\.","",checker.group(1))
           newer = re.sub(r"youtube\.com","youtu.be",new)
           newest = re.sub(r"https?","https",newer)
           newestest = re.sub(r"embed/","",newest)
           return newestest




...


if __name__ == "__main__":
    main()
