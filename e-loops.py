# """LOOPS"""

# # Loops in python allow us to  execute  a block of code multiple times without rewriting it...
# i="hello"
# for i in range(1, 100):
#     print(i)

# # When we know the number of iterations we will use a FOR LOOP......
"""FOR LOOP"""
# a= range(1,20,1)

# for i in a:
#     print(i)


# for i in range(16,0,-1):
#     print(i)


# # Print a table of 5...
# n=int(input("Enter a table you want? "))
# for i in range(n,(n*10)+1,n):
#     print(i)


# LOOPS FOR STRINGS
# a = "RiiAnii"
# for i in range(len(a)):
#     print(a[i])


# a="Rii"
# for char in a:
#     print(char)


# Break Continue Else

# for i in range(1,21):
#     if i==15:
#         break
#     else:
#         print(i)


# for i in range(1,21):
#     if i==15:
#        continue
#     else:
#         print(i)

# for i in range(1,21):
#     if i==15:
#         print("break stat is executed")
#         break
#     print(i)
# else:
#     print("Break stat is not executed")


""""Questions"""

# # 1..
# n= int(input("Enter an integer"))

# for i in range(n):
#     print("hello world")


# # 2..
# n= int(input("Enter an integer"))
# for i in range(1,n+1):
#     print(i)

# # 3..
# n= int(input("Enter an integer"))
# for i in range(n, 0, -1):
#     print(i)


# # 4..
# n= int(input("Enter a table you want?"))
# for i in range(n,(n*10)+1,n):
#     print(i)

# # 5..
# n = int(input("please tell your number:- "))

# sum = 0 
# for i in range(1,n+1):
#     sum = sum + i
# print(f"your sum is {sum}")


# # 6..
# n = int(input("please tell your number:- "))

# fact = 1 
# for i in range(1,n+1):
#     fact = fact * i
# print(f"your factorial is {fact}")


# # 7..
# n = int(input("tell your number :- "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
# print(f"your even and odd sum are {even} , {odd}")


# # 8..
# n =int(input("which number factors you want :- "))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)

# # 9..        (perfect number : a number whose sum of factors is equal to the number itself)....
# n = int(input("check your number is perfect or not :-"))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i

# if sum == n:
#     print("your number is perfect")
# else:
#     print("not a perfect number")


# # 10..
# n = int(input("check your number is prime or not  :-"))

# count = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2:
#     print("your number is prime")
# else:
#     print("your number is not prime")



# # 11..
# a = "RiiAnii"
# for i in range(len(a)-1,-1,-1):
#     print(a[i])


# # 12..
# a = "NAMAN"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# if b == a:
#     print("your string is pallindrome")

# else:
#     print("its not a pallindrome")


# # 13..
# a = "sdfsogn12413@#$%^&U"

# char = 0
# dig = 0
# spchr = 0

# for i in a:
#     if i.isdigit():
#         dig +=1 
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr +=1 
# print(f"your digits are {dig}\nyour alphabets are {char}\nyour special characters are {spchr}")
# print(dir(str))

"""WHILE LOOP"""

# # When we don't know the number of iterations we have to use but we know a condition that determines when to stop  we will use WHILE LOOP....

# num=1
# while num<=30:
#     print(num)
#     num+=1


"""QUESTIONS"""


# # 1..
# a = int(input("tell your number"))
# rev = 0
# while a > 0:
#     rev = rev *10 + a % 10
#     a = a //10
# print(rev)


# # 2.
# a = int(input("tell your number"))

# copy = a
# rev = 0
# while a > 0:
#     rev = rev *10 + a % 10
#     a = a //10
# if copy == rev:
#     print("pallindromic number")
# else:
#     print("not a pallindromic number")
