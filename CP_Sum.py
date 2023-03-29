# Task
"""Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous
number."""
num = int(input("Enter the input number:"))
previous_num = 0

# loop from 1 to num
for i in range(0, num):
    # iterating over loop
    sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", sum)
    # modify previous number
    # set it to the current number
    previous_num = i