# Task
"""An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It
corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year
contains a leap day.
In the Gregorian calendar, three conditions are used to identify leap years:
The year can be evenly divided by 4, is a leap year, unless: The year can be evenly divided by 100, it is NOT a leap
year, unless: The year is also evenly divisible by 400. Then it is a leap year. This means that in the Gregorian
calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years."""

"""Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return 
False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary 
to complete the is_leap function. """
# Sample Test cases
# 2000 - True
# 2100 - False
# 2400 - True
# 3455 - False
# 1990 - False
# 1992 - True
# For Year 2100 check
"""year = 2100
if year % 100 == 0:
    print("Leap")
else:
    print("Not Leap")"""


# Input Format: Read year,the year to test.
# Output Format: The function must return a Boolean value (True/False).
# Sample Input : 1990
# Sample Output : False """ Method 1:This part will  not pass all the test cases"""
# Explanation : 1990 is not a multiple of 4 hence it's not a leap year.
# CODE:
def is_leap(year):
    """ Method 1:This part will  not pass all the test cases"""
    # if year % 4 == 0 and year % 100 != 0:
    #   if year % 400 == 0 and year % 100 == 0:
    #      return True
    # elif year % 4 != 0:
    #   return False
    # For Year 2100 check
    # It returns none
    """Method 2: This part will pass all the test cases"""
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("Enter the year:"))
print(is_leap(year))
