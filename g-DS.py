# Data  structures are used to store, organize, and manipulate data efficiently. Python provides several built-in data structures..

# And for storing multiple values we will again use variables..

"""IN-BUILD DATA STRUCTURES"""
# Now in python we have 4-types of in-built data structure..
# LIST
# TUPLE
# DICTIONARY 
# SET..


"""CUSTOM DATA STRUCTURES"""
# STACK
# QUEUE
# LINKED LIST
# GRAPH 

# Around these data structure there are some algorithms like searching algorithms, sorting algo...

"""List"""
# Mutable : changed after creation
# Duplicates : used to store multiple values so duplicates means same value occuring multiple time. list allows this...
# Ordered : List maintains ordered data structure maintains the sequence of elements as they were inserted . This means you can access elements using their position (index)...
# Heterogenous : List have heterogenous nature that means we can have multiple data types inside the list...  


a=[12,11.14,15]

# #1st way using index

for i in range(len(a)):
    print(a[i])

# #2nd way directly on values

for i in a:
    print(i)


"""QUESTIONS"""

"""1"""
# l = [-45,67,12,-68,-69,34]

# print("positive elements are ")
# for i in l:
#     if i >= 0:
#         print(i)
# print("negitive elements are")

# for i in l:
#     if i < 0:
#         print(i)

"""2"""
# l = [12,435,67,89,23,25,69]

# sum = 0

# for i in l:
#     sum = sum + i

# print(sum/len(l))


"""3"""
# l = [12,567,43,235,347,568,45,7]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f"your largest number is {largest} at index {index}")


"""4"""
# l = [12,16,13,19,17]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i
# print(sec_largest, largest)


"""5"""
# a = [12,13,18,15,16]

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")


"""TUPLE"""
# Immutable
# Duplicate
# Ordered
# Heterogenous

a = (1,2,3,4,5,5,5.5,print(),"hello")
count = a.count(5)
print(count)


a = (1,)
print(type(a))


"""SET"""
# Mutable
# Duplicate
# UnOrdered
# Heterogenous

a = {1,8,9,"hello",2,3,4,5}
for i in a:
    print(i)

# a = {8,1,2,3,4}
# a.clear()
# print(a)


# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# b -= a
# print(b)



# d = {10:100,20:200,30:300,40:400}

# d[10] = 100 #updating
# d[50] = 500 # creating
# del d[30] # deleting 

# print(d)

# d = {10:100,20:200,30:300,40:400}

# print(d.items())

# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}


# for i in d2:
#     d1[i] = d2[i]

# print(d1)

# d1 = {10:100,20:200,40:300}
# sum = 0

# for i in d1:
#     sum = sum + d1[i]

# print(sum)

"""DICTIONARY"""
# Mutable
# Duplicate
# Order
# Heterogenous
# a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]

# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] +=1 
#     else:
#         d[i] = 1

# print(d)


# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]
