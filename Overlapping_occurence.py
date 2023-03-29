# TASK
"""In this challenge, the user enters a string and a substring. You have to print the number of times that the
substring occurs in the given string. String traversal will take place from left to right, not from right to left.

Input Format:mThe first line of input contains the original string. The next line contains the substring.
Output Format: Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input:
ABCDCDC
CDC
Sample Output:
2"""


# CODE:
# Defining a function
def count_string(string, sub_string):
    # Initializing count value to zero
    count = 0
    # count length of original string using len() function
    # Iterating over for loop
    for i in range(len(string)):
        # It takes from I index and checks with substring
        if string[i:].startswith(sub_string):
            # Incrementing the count value
            count += 1
    return count


# Getting input from the user
string = input("Enter the original sting: ").strip()
sub_string = input("Enter the sub_string: ").strip()
Occurence = count_string(string, sub_string)
print("The number of occurence of substring over original string is: ", Occurence)

# strip() method explained:
"""The strip () method removes given characters from start and end of the original string. By default, strip () function removes white spaces from 
start and end of the string and returns the same string without white spaces."""