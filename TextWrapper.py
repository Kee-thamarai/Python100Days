# TASK
"""You are given a string S and width w. Your task is to wrap the string into a paragraph of width w.
Sample Input :
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output :
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ"""
# CODE
import textwrap


# Defining a function
def wrap(string, width):
    # Wrapping text
    wrapper = textwrap.fill(string, width)
    return wrapper


# Getting input from the user
string, width = input("Enter the wrapping string: "), int(input("Enter the width: "))
result = wrap(string,width)
print(result)