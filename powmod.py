# TASK
"""Powers or exponents in Python can be calculated using the built-in power function. Call the power function ab as shown below:
>>> pow(a,b)
or
>>> a**b
It’s also possible to calculate ab mod m.
>>> pow(a,b,m)
This is very helpful in computations where you have to print the resultant % mod.
You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).
Input Format: The first line contains a, the second line contains b, and the third line contains m.
Sample Input:
3
4
5
Sample output:
81
1"""
# CODE:
# Getting input from the user
num1 = int(input("Enter the first input: "))
num2 = int(input("Enter the second input: "))
num3 = int(input("Enter the third input: "))
# Performing power operation
power = pow(num1, num2)
# Printing power
print("The power value of " + str(num1) + " and " + str(num2) + " is: ", power)
# Performing mod operation
powermod = power % num3
# Printing mod-power
print("The ModPower value of " + str(power) + " and " + str(num3) + " is: ", powermod)
