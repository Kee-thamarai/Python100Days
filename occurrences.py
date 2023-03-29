# Importing packages
"""RegEx can be used to check if a string contains the specified search pattern. Python has a built-in package called re"""
import re

# Getting input from the user
String = input("Enter the string:").strip()
Sub_String = input("Enter the sub_string:").strip()
# Find number of times occurrences in string using len() function
Occurrences = len(re.findall(Sub_String, String))
print("The number of occurrences in string: ", Occurrences)
# Printing the occurrences in list
Str_Occurrences = re.findall(Sub_String, String)
print("The occurrences in string is: ", Str_Occurrences)


