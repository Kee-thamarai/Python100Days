""" PRINT Statement in Python ---> Printing is mostly used for displaying information to the console, whether it's
 showing a certain message or computational result. But it's also used for debugging purposes."""
# Syntax ---> print()
print("Welcome to python world!!!")  # Output: Welcome to python world!!!

""" The print() function has no return value.
This will just output a blank line to the console in such a case.It's similar to hitting they Enter key on your keyboard 
when writing in a word processor.Just like the Enter key creates a new line and moves the cursor to a new line,
in the same way calling print() with no arguments displays an empty line."""
print()
# Printing new line
print("Hello")  # Output is Hello
print("World")  # Output is World
# Removing default new line ---> you can explicitly change the value of end to an empty string, "".
# Syntax : end = ""
print("Hello", end="")  # Output is HelloWorld
print("World")
# Print using any character in between end like seperator.
print("Hello", end="*")  # Output is Hello*World
print("World")

# If you have a set string or phrase you want to print, you can store it in a variable and pass the
# variable name as the argument to print().
print()
Greeting = "Hello World"
print(Greeting)  # Output is Hello World

# More than one object passed as arguments (*object) by """separating""" each argument with a comma.
print()
print("Welcome", "Python")  # Output is Welcome Python
# Another Way Objects Are Separated in the print() Function
print("Welcome", "Python", sep="--->")  # Output is Welcome--->Python

# Printing arguments with string literal and a variable.
print()
Wishing = "Hello"
print(Wishing, "Kiruthika")  # Output is Hello Kiruthika

# concatenate with the addition operator
print()
Name = "kiruthika"
print("Hey " + Name)  # Output is Hey kiruthika

# print integer
print()
print(7)  # output is 7

# print floats
print()
print(7.0)  # output is 7.0

# print complex
print()
print(1j)  # output is 1j

# print a list
print()
print([10, 20, 30])  # output is [10,20,30]

# print a tuple
print()
print((10, 20, 30))  # output is (10,20,30)

# print a dictionary
print()
print({"language": "Python", "field": "data science"})
# output is {"language": "Python", "field": "data science"

# print a set
print()
print({"autumn", "winter", "spring", "summer"})
# output is {"autumn","winter","spring","summer"}

# print a bool
print()
print(True)  # output is True
print(False)  # output is False

"""How to Direct the print() Output to a File in Python. Means have a text file and want to add some text using the 
print() function.
To open and write to a file in Python, you call the open() function. Inside it you include the name of the file, 
output.txt in this case, and the -w mode, meaning for writing only."""
with open('../output.txt', 'w') as f:
    print('Hello World!', file=f)
# After execution when you see the project location output.txt file is created.