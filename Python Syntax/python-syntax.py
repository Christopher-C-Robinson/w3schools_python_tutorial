# Python uses indentation to indicate a block of code.

if 5 > 2:
    print("Five is greater than two!")

# Python will give you an error if you skip the indentation:

if 5 > 2:
print("Five is greater than two!")

# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:

if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")

# In Python, variables are created when you assign a value to it:

x = 5
y = "Hello, World!"

# Comments start with a #, and Python will render the rest of the line as a comment:

#This is a comment.
print("Hello, World!")
