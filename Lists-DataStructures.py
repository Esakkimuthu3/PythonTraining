#Lists:

#How to create a collection of data using list

empty =  []
print(empty)

str = "DATA"
str = str.list()
print(str)

#MAtrix - Nested List

matrix = [['a','b','c'],
          ['d','e','f']]

print(matrix)

# Indexing and Slicing ( Access and Read)

#Indexing:

matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
print(matrix[1])
print(matrix[1][1])

#Slicing

#Unpacking:

person = ['Ashwin', 29 , 'Data Engineer', 'Spain']

# - Unpacking:

name, age, role, country = person

print(name)

# - Asterick

name , *details, country = person

print(*details)

# - Underscore_

person = ['Ashwin', 29 , 'Data Engineer', 'Spain']

name, _ , role , _ = person

print(name)

#Order:

L= ['a','n','b','d']
a= list(reversed(L))
print(a)

matrix = [['d','e','f'],
          ['a','b','c'],
          ['g','h','i']]

matrix.sort(reverse = True)
print(matrix)

matrix[1].sort()
print(matrix)

#Iterator:

letters = ['a','b','c']
numbers = [1,2,3,4]

for i in map(str.upper, letters):
    print (i)  



for l , n in zip(letters,numbers):    #zip
    print(l , n)

for l in reversed(letters):            #reverse
    print(l)

for index, value in enumerate(letters):     #enumerate
    print(index, value)


letters = ['a','b','c','2','45']

for i in filter(str.isnumeric,letters):
    print(i)

