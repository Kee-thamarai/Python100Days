# TASK
"""One of the built-in functions of Python is divmod, which takes two arguments and returns a tuple containing the
quotient of a/b first and then the remainder a.

For example:
>>> print divmod(177,10) >>> (17, 7)
Here, the integer division is 177//10 => 17 and the modulo operator is 177%10 => 7.

Task
Read in two integers, a and b, and print three lines.
The first line is the integer division a//b (While using Python2 remember to import division from __future__).
The second line is the result of the modulo operator: a%b.
The third line prints the divmod of a and b.

Input Format: The first line contains the first integer, a, and the second line contains the second integer, b.
Output Format: Print the result as described above.

Sample Input:
177
10
Sample Output:
17
7
(17, 7)"""
# CODE:
# Getting input from the user
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
# Printing integer division result
print(num1 // num2)
# Printing modulo result
print(num1 % num2)
# Printing using div-mod operation
result = divmod(num1, num2)
print(result)