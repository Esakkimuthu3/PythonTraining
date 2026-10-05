#Casting: Changing the data type of a variable from one datatype to another using int() , float(), str()...

a = "10"
a = int(a) #changing from string "10" to integer 10.
b = 20 #Whatever that belongs inside quotes is string
print(a +b)

#UserInput: Receives input for a variable from user using input().

a = int(input()) # Ususally, if the variable uses input() alone to receive input, then the datatype of that input will be String in default.
# So we need Typecasting to receive the different datatype apart from string.
b = 20
print(a + b)

#Problem 1:

name = input("Enter your name:  ")
age = int(input("Enter your age:  "))

print("My name is:",name)
print("My age is:",age)

#Problem 2:

a,b,c = int(input()), int(input()), int(input())
Multiply = a*b*c
Add = a+b+c
Divide = Multiply / Add
print(Divide)


