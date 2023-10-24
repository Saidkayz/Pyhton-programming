# It uses a function called `check_leap_year` that takes a year as an argument.
# The function checks if the year is divisible by 4.
# If it is, it checks if the year is divisible by 100. If it is,
# it checks if the year is divisible by 400.
# If the year is divisible by 400, the function returns "Leap Year".
# Otherwise, it returns "Not a Leap Year". If the year is not divisible by 4,
# the function returns "Not a Leap Year".
# The result is then printed to the console.
def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap Year"
            else:
                return "Not a Leap Year"
        else:
            return "Leap Year"
    else:
        return "Not a Leap Year"

year = int(input("Enter a year: "))
print(check_leap_year(year))

