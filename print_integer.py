# Task
"""The included code stub will read an integer, n, from STDIN. Without using any string methods, try to print the
following: 123...n Note that "..." represents the consecutive values in between.
Example: n = 5.
Print the string 12345.
Input Format: The first line contains an integer n.
Output Format: Print the list of integers from 1 through n as a string, without spaces."""
# CODE:
# Getting input from the user
n = int(input("Enter the input:"))
# Iterating the values through for loop by range
for i in range(1, n + 1):  # As range() function takes upto n-1 ,we concluded n+1 as range.
    print(i, end="")       # Printing i and end is defined to no new line
