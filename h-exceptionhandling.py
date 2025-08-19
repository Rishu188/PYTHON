"""Exception Handling"""
# Errors occur due to mistakes in the code that prevent it from running. These can be syntax errors or logical errors...

# Syntax 
# indentation

# Exceptions
# Exceptions are unexpected events or errors that occurs during the execution of a program, which disrupts the normal flow of the program...

#e.g.
# a= int(input("enter a number:"))
# print(10/a)   # if the value of a is 0 then it will give error that is called Exception....

""" Exception Handling"""
# try : wrap the block of code that might cause an exception..
# except : Handle the exception if it occurs..
# else : Run code only if no exception occurs..
# finally
# raise

# a= int(input("enter a number:"))
# try:
#     print(10/a)

# except ZeroDivisionError:
#     print("sorry you cannot divide by 0")


# a= int(input("enter a number:"))
# try:
#     print(10/a)

# except Exception as err:
#     print(f"sorry there is an error as {err}")

# else:
#     print("there is no exception")

# finally:
#     print("always run")

# salary=int(input("enter salary: "))

# try:
    
#     if salary < 10000 or salary > 50000:
#        raise ValueError("salary must be between 10000 and 50000")
    
#     else:
#        print("accepted")

# except Exception as err:
#    print(f"an error occured as {err}")

# print("the club will start soon")