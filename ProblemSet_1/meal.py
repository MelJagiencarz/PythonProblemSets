def convert(time):
    hours, minutes = time.split(':')
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60.0

def main():
    time = convert(input("What time is it? "))

    if time >=7.0 and time <=8.0:
        print("Breakfast time")

    elif time >=12.0 and time <=13.0:
        print("Lunch time")

    elif time >=18.0 and time <=19.0:
        print("Dinner time")

    else:
        print("")


if __name__ == "__main__":
    main()

