def add_time(start, duration):
    currTime = float(start.replace(":", ".").replace("PM", ""))  # output -> 3.00
    toAddTime = float(duration.replace(":", "."))  # output -> 3.10
    newTime = str(format(currTime + toAddTime, ".2f"))

    print(newTime.replace(".", ":"))


add_time("3:00 PM", "3:10")

# To be continued...