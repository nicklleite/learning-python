# Section 05
# Errors & exceptions in Python
# Syntax error, logical error * exceptions

# def function1(a, b):
#     print(a / b)
#
#
# function1(2, 0)
# print('Not executed due to the Exception')

# Handling exceptions
# try:
#     a = 20
#     b = 5
#     print(a/b)
# except ZeroDivisionError:
#     print('There is a divide by zero error')
# finally:
#     print('This is going to execute no matter what!')

# Handling files
# Reading data from file

# file = open('section05-demo.txt', 'r')
# content = file.read()
# content = file.readline()
# print(content)

# Writing content to the file
# file = open('section05-demo.txt', 'w')
# file.write("This is the text writen to the file")

# Appending to the file
# file = open('section05-demo.txt', 'a')
# file.write("This is the first line")
# file.write("This is the second line")
# file.close()

# #############################################################################
# Coding challenge part 5
#
# - Write a function which would divide two numbers, design the function in a
#   manner that it handles the divide by zero exception.
# #############################################################################
def division(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("The second parameter can't be zero!")


# division(10, 5)


# #############################################################################
# Coding challenge part 6
#
# 1. Write Python code to open a file named demo.txt and write some random data
# into it.
#
# 2. Open the file, read the contents and display them as output.
#
# 3. Write python code to add additional text to the existing file on a new
# line without deleting the previous contents.
# #############################################################################

file = open("section05-demo.txt", 'w')
file.write("This is a random content")
file.close()

file = open("section05-demo.txt", 'r')
content = file.read()
print(content)
file.close()

file = open("section05-demo.txt", 'a')
file.write("\nThis is more to the previous random content")
file.close()
