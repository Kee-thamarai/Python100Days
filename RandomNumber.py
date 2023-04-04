# Import random
import random

# Get input from the user
num = int(input("Enter the input: "))
# Generating random number using randint()
random_number = random.randint(0, num)
# Printing result
print("The random number between 0 to " + str(num) + " is: ", random_number)
