print("Hello World")

a = 23  # int
b = "Pencil"  # String
c = 23.2  # float

d = "D"  # character


print (a,  b, c, d )

print(a+c)

# to know the datatype of variable use type(variable_name)

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Operators:

a = "baraa"
print("info@datawith",a,".com")

a= 100
print(a.bit_length())

a = "968-maria, (D@t@ Engineer );; 27y   "
role = a[12:25].replace("@","a").lower()
print("name:",a[4:9] , " | " "role:" , role , " | " "age:" + a[30:32])

username = ""
age = 20

# Check conditions using logical operators
if username and age >= 18:
    print("Valid user and adult.")
else:
    print("Invalid username or under age.")

email="ashwin@gmail.com"
a = email and "@" in email and email.endswith(".com")
print (a )   

user = "ashwin"
a = isinstance(user, str) and user is not None and len(user) > 5
print(a)

is_admin = False
is_moderator = False
is_banned = False
is_verified = True
print(is_admin or is_moderator and not is_banned or is_verified)