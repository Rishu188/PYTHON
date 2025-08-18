"""FUNCTIONS"""
# Functions in python group reusable code into a block that can be executed by calling the functions name. This helps avoid repetition and makes programs modular and readable...
# There are many in-build functions modular and readable...

# def Rii():
#     print("hii my name is rii")

# Rii()


"""Parameters and Arguments"""
# Parameters are variables listed inside the function definition... For making the function we have to accept inside the parenthesis of the function....

# def sum(a, b):   #parameters..
#     print(f"sum of numbers:{a+b} ")
# sum(12, 13) #Arguments..

"""ARGUMENTS"""
# Arguments are the values passed to a function when it is called...

# Types of Arguments...

# Positional Argument
# def sum(a, b):   #parameters..
#     print(f"sum of numbers:{a+b} ")
# sum(12, 13) #Arguments..

# # Default Argument
# def rii(a, b=45):  # default parameter
#     print(f"the sum is {a+b} ")

# rii(12, 34) # default arg. replace

# # Keyword Argument
# def rii(name, age):
#     print(f"hii, I'm Rishu {name}, my age is {age} ")

# rii(age=20, name="Rii")


# # Check string is palindrome or not......

# def palindrome(st):
#     rev=""
#     for i in range(len(st)-1,-1,-1):
#         rev=rev + st[i]

#     if rev == st:
#         print(f"{st} is palindrome")
#     else:
#         print(f"{st} is not a palindrome")
# palindrome("NAMAN")
# palindrome("rISHU")


# # return
def rii():
    return "hii how are you"

print(rii())