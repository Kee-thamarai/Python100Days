# Task
"""The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i2 .
Example: n=3.
The list of non-negative integers that are less than n=3 is[0,1,2] . Print the square of each number on a
separate line.
0
1
4
Input Format: The first and only line contains the integer,n .
Output Format: Print n lines, one corresponding to each i ."""

# CODE:
# Getting input from the user
n = int(input("Enter the number:"))
# Using for loop from 0 to n range
# Explanation of for loop
# For example,  n = 3
"""1st iteration---->i=0--->i*i=0*0=0
   2nd iteration---->i=1---->1
   3rd iteration---->i=2----->4"""
# range() function takes until n-1
for i in range(0, n):
    # square the numbers
    square = i * i
    # Printing the square of each number
    print(square)


