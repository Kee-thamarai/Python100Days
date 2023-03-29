# Task
"""Given an integer, perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird """
""" Input Format
# A single line containing a positive integer.
# Constraints
# 1<=n<=100
# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.
# Sample Input 
# 3
# Sample Output 
# Weird """

# CODE:
# Getting input from the user
n = int(input("Enter the number:").strip())  # strip() ---> Remove spaces at the beginning and at the end of the string.
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and n in range(2, 6):  # range() ---> takes from 2 to n-1(6-1 = 5)
    print("Not Weird")
elif n % 2 == 0 and n in range(6, 21):
    print("Weird")
else:
    print("Not Weird")
