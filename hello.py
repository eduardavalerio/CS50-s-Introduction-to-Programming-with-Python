print("Hello, world")

# Function is like an action that lets you do something in the program.
# Python comes with predetermined set of functions.
# PRINT IS A FUNCTION 

# Argument is an input to a function. 
# HELLO, WORLD IS AN ARGUMENT.

# Bugs are mistakes you made in a program. 

input("What is your name?")
print("Hello, Eduarda")

# Return values feature of some functions which is that they can have return values.
# to use these return values is required VARIABLES (in this case, 'name' is a variable).

name = input("What is your name?") # One equal sign (=) is the assingment operator. 
print("Hello,", name)

# STRING is a sequence of text
# the function input only expect strings. 
# a technical term of string is STR.
# on python's documentation have this function: 'print(*objects, sep=' ', end='\n', file = sys.stdout, flush = False)
# \n means 'new line', sep means separator

# 'print(*objects, sep=' ', end='\n', file = sys.stdout, flush = False), 'sep', 'end' are called PARAMETERS.

name = input("What is your name?")
print(f"Hello, {name}") #using a format string, or an F string, it's a special string.
 

## STRINGS 
# Strings themselves come with a lot of funcionality 
# Can see all of that in Python's documentation (docs.python.org/3/library/stdtypes.html#string-methods)

# String functions 
name = name.strip() # To remove white space from str. 
# Using the name of str (name) and .(function), in this case, the function is 'strip'.

name = name.capitalize() # Capitalize user's name, just the first name.

name = name.title() # Capitalize the first letter of all words. 

# It is possible to chain the string functions.
name = name.strip().title()

##### ALL CODE #####
name = input("What is your name?")
name = name.strip().title() 
print(f"Hello, {name}")

# split user's name into first and second name 
first, last = name.split(" ") # possible just first name and last name (2)
print(f"Hello, {first}")


## DEFINE (DEF)
# define, create, invent your own functions.
def hello(to="world"):
    print("hello,", to)

hello()
name = input("What is your name?")
hello(name)