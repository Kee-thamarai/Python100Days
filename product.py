# TASK
"""Given two integer numbers return their product only if the product is equal to or lower than 1000, else return
their sum."""
# Getting input from the user
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
# Calculating product
prod = num1 * num2
# Using if loop to check whether the value of product is less than or equal to 1000
if prod <= 1000:
    print("The product of two numbers are:", prod)
else:
    print("The product is grater than 1000")

