""" CONDITIONAL STATEMENTS"""
#  Conditional statements in python allow decision making by executing different blocks of code based on conditions....

#if: Execute if the conditions is True
# if-else : Execute if True, another if  False
#if-elif-else: Checks multiple condition in sequence...


# num=10
# if num > 9:
#     print("i will do task A")

# else:
#     print("i will do task B")


# money = int(input("please provide me the money :- "))
# if money == 10:
#     print("I will have a choco bar icecream")
# elif money == 20:
#     print("I will have a mangodolly")
# elif money == 30:
#     print("I will have a frosty")
# else:
#     print("I will have a cone")


# Questions
# 1..
# a= int(input("enter a number1:"))
# b= int(input("enter a number2:"))

# if a > b:
#     print(" a is greater than b")
# else:
#     print("b is greater than a")

# 2..
# gender = input("please tell your gender as character (Male or Female):")
# if gender == 'Male' or gender == 'male':
#     print("Good morning SIR")
# elif gender == "Female" or gender == 'female':
#     print("Good morning MAM")

# else:
#     print("Unidentified gender")


# 3..
# num = int(input("enter a number : "))
# if num%2 == 0:
#     print("even number")
# else:
#     print("Odd number")


# 4..
# name = input("please tell your name : - ")
# age = int(input("now tell your age :- "))

# if age >=18 :
#     print(f"hello {name} you are a valid vote")

# else:
#     print(f"hello {name} you are not a valid vote")


# 5..
# year = int(input("tell your year :- "))

# if year %100 == 0 and year %400 == 0:
#     print("Its a leap year")

# elif  year %100 != 0 and year %4 ==0:
#     print("Its a leap year")

# else:
#     print("its a normal year")


# If-elif ladder
t = int(input("please tell the temprature : "))
if t < 0:
    print("Freezing cold")

elif t >= 0 and t <10:
    print("very cold")

elif t >= 10 and t <20:
    print("cold")

elif t >= 20 and t <30:
    print("plesant")

elif t >= 30 and t <40:
    print("hot")

else:
    print("temprature is very hot ")
