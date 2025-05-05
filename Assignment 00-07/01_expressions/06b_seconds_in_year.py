
# useful constant to help make the math easier and cleaner! 

DAYS_PER_YEAR : int = 365
HOURS_PER_DAY : int = 24
MINUTES_PER_HOUR : int = 60
SECONDS_PER_HOUR : int = 60

def main():
    print("There Are " + str(DAYS_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_HOUR) + "Seconds in a year!")

# There is no need to edit code when we want to call the function.
# calling the function is necessary to show result.

if __name__ == "__main__":
    main() # this is the function name which we are calling at the end of the project to understand python that to run program.