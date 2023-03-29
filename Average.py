# TASK
"""Task The provided code stub read in a dictionary containing key/value pairs of name:[Marks] for a list of
students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example
marks key: value pairs are
'alpha':[20, 30, 40]
'beta':[30, 50, 70]
query_name = 'beta'
The query_name is 'beta'. beta's average score is (30 + 50 + 70)/3 = 50.0.

Input Format The first line contains the integer n, the number of student's records. The next n lines contain the
names and marks obtained by a student, each value separated by a space. The final line contains query_name ,
the name of a student to query.

Constrains
2 ≤ n ≤ 10
0 ≤ marks[i] ≤ 100
length of the marks array = 3
Output Format
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output 0
56.00

Explanation 0
Marks of Malika are {52, 56, 60} whose average is (52 +56 +60)/3 ⇒  56"""

# *line
"""It splits a string by white-spaces (or newlines and some other stuff), assigns name to the first word, then assigns 
line to the rest of the words, to see what it really does:
>>> s = 'a b c d e f'
>>> name, *line = s.split()
>>> name
'a'
>>> line
['b', 'c', 'd', 'e', 'f']
"""

# CODE:
# Getting input from the user
n = int(input("Enter the number of inputs:"))
# Empty dictionary
student_marks = {}
for i in range(n):
    # unpacking operator "*" to unpack the list of scores from the input
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
# finding the percentage in python
output = list(student_marks[query_name])
average = sum(output) / len(output)
print("%.2f" % average)

# CODE EXPLANATION
"""uses a for loop to take "n" number of inputs, where each input consists of a name followed by multiple values 
separated by a space. The name is used as the key in the dictionary "student_marks" and the rest of the values are 
used as a list of scores as the value for that key. Then it takes another input "query_name" from the user.
Using this input it accesses the value of the key in the dictionary "student_marks" and assigns it to variable 
"na" . Then it calculates the average of the values in "na" and prints the result in a formatted manner with 2 
decimal places."""