import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    m = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    if m:
        for d in m.groups():
            if int(d) < 0 or int(d) > 255:
                return False
            continue
        return True
    else:
        return False

if __name__ == "__main__":
    main()
