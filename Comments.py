# COMMENTS
"""The comments are descriptions that help programmers to understand the functionality of the program. Thus, comments are
necessary while writing code in Python.
In Python, we use the hash (#) symbol to start writing a comment. The comment begins with a hash sign (#) and
whitespace character and continues to the end of the line."""

# Single-line Comment
"""In Python, single-line comments are indicated by a hash sign(#). The interpreter ignores anything written after 
the # sign, and it is effective till the end of the line."""
# welcome message
print('Welcome to PYTHON world!!!')
# As you can see in the above program, we have added the comment ‘welcome message’.

# Multi-Line Comments
"""In Python, there is no separate way to write a multi-line comment. Instead, we need to use a hash sign at the beginning of
 each comment line to make it a multi-line comment"""
# This is a
# multiline
# comment
print('Hello')

# Inline Comments
"""An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces 
from the statement. They should start with a # and a single space."""
a = 1
b = 2
print(a + b)  # Result must be 3 //Inline comment
print()

# Block Comments
"""Block comments are used to provide descriptions of files, classes, and functions. We should add block comments at the 
beginning of each file and before each method."""


def message_writer(msg):
    # We may need to do it this way in the future
    # new_msg = "Message Writer says: "
    # new_msg += msg
    # print(new_msg)

    print("Message Writer says: " + msg)


message_writer("Loving' it!")

# Docstring Comments
"""Python docstrings are the string literals that appear right after the definition of a function, method, class, 
or module. Let's take an example."""


def square(n):
    '''Takes in a number n, returns the square of n'''
    return n ** 2


print(square.__doc__)


# Another Example
def bonus(salary):
    """Calculate the bonus 10% of a salary ."""
    return salary * 10 / 100
