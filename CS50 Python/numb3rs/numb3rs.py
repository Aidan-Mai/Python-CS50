import re



def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]+\.+[0-9]+\.+[0-9]+\.+[0-9]+$", ip):
            list_of_numbers = ip.split(".")
            for n in list_of_numbers:
                if int(n) < 0 or int(n) > 255:
                    return False
            return True
    else:
        return False







...


if __name__ == "__main__":
    main()
