# TASK
"""You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
For example: Www.HackerRank.com → wWW.hACKERrANK.COM,Pythonist 2 → pYTHONIST 2
Input format: A single line containing a string S.
Output format: Print the modified string S."""


# Defining function
def swap_case(s):
    string = s.swapcase()
    return string


# Getting input from the user
s = input("Enter the string: ")
result = swap_case(s)
print("The swapcase string is:", result)
