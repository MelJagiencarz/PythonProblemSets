import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    RE = re.search(r'(\d{1,2})(:\d{2})?\s+(AM|PM)\s+to\s+(\d{1,2})(:\d{2})?\s+(AM|PM)', s)
    if RE:
        start_hour = int(RE.group(1))
        finish_hour = int(RE.group(4))

        if start_hour < 12 and RE.group(3) == 'PM':
            start_hour = start_hour + 12
        elif start_hour == 12 and RE.group(3) == 'AM':
            start_hour = 00
        if finish_hour < 12 and RE.group(6) == 'PM':
            finish_hour = finish_hour + 12
        elif finish_hour == 12 and RE.group(6) == 'AM':
            finish_hour = 00


        start_mins = RE.group(2)
        finish_mins = RE.group(5)

        if not start_mins:
            start_mins = ':00'
        if not finish_mins:
            finish_mins = ':00'
        if int(start_mins.strip(':')) > 59:
            raise ValueError
        if int(finish_mins.strip(':')) > 59:
            raise ValueError

        return f"{start_hour:02}{start_mins} to {finish_hour:02}{finish_mins}"

    else:
        raise ValueError

if __name__ == "__main__":
    main()
