#Set() : set is a collection of non repetitive elements


# D/f b/w dictionary and set

# agar key value pair rahe tho dictory nai tho set

# example of dictionary
# set1 = {
#     1:"1",
#     2:'2',
#     4:'3'
#     }

# print(type(set1))

# example of set 
# set2 = {1,2,4}
# print(type(set2))

# Some tricky parts

empty = {}

#initializing with empty curly braces then it is a dictionary

# print(type(empty))

# in case if you want to initialise the set as empty

# emptySet = set()

# print(type(emptySet))

# methods in set

alpha = set()

# alpha.add(1)
# print(alpha)


# in this method I cant add mutable elements like list and Dictionary but I can add immutable methods and elements like tuple

alpha.add((1,2,3,4))
print(alpha)



