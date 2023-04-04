# Getting input from the user
n = int(input("Enter the input: "))
# Iterating through for loop
# Outer loop
for i in range(1, n + 1):
    # Inner loop
    for j in range(1, n + 1):
        print(i * j, end=" ")
    print()

