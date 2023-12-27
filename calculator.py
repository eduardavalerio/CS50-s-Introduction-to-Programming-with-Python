## INTEGER (INT)
# numbers with no decimal point 

x = 3
y = 7

z = x + y
print(z)

# using input function
x = input("What's x?")
y = input("What's y?")

z = x + y
print(z)

# In python you can convert one type of data (STR) to another type of data (INT)

x = input("What's x?") # when you use the function input, the value, even though it's a number, it's manipulate like str
y = input("What's y?")

z = int(x) + int(y)
print(z)

x = int(input("What's x?")) 
y = int(input("What's y?"))
print(x + y) # Don't need the variable 'z'.

# code with no variables
print(int(input("What's x?")) + int(input("What's y?")))

# FLOAT FUNCTION to use numbers with decimal point 
x = float(input("What's x?"))
y = float(input("What's y?"))
print(x + y)


## ROUND FUNCTION
# 'round(number[,ndigits])
# [,] this means something opitional -> specify more precisely the number of digits that you want the round function
x = float(input("What's x?"))
y = float(input("What's y?"))
z = round(x / y, 3) # rount to three decimal points.
print(z)

