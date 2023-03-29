# Statements
# A statement is an instruction that a Python interpreter can execute.

# statement 1
x = 20
# statement 2
print(x)

# Add multiple statements on a single line separated by semicolons.
# two statements in a single
l = 10; b = 5
# statement 3
print('Area of rectangle:', l * b)

# Multi-Line Statements ---> 2 categories -- implicit and explicit
# Explicit continuation ---> Extend the statement over multiple lines using line continuation character (\).
Sum = 10 + 20 + \
      30 + 40 + \
      50 + 60 + 70 + \
      80 + 90 + 100
print("Sum is: ", Sum)

# Implicit continuation ---> Multiple line can be covered in ().
Add = (10 + 20 +
       30 + 40 + 50 +
       60 + 70)
print("Addition is: ", Add)
# For the implicit we can us [],{}.
# list of strings
names = ['Emma',
         'Kelly',
         'Jessa']
print("List:" , names)

# dictionary name as a key and mark as a value
# string:int
students = {'Emma': 70,
            'Kelly': 65,
            'Jessa': 75}
print("Dictionary: " , students)





