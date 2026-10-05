a = int(input("Enter a number:  "))
if(a >= 10):
    print("The number is greater or equal to than 10")
elif(a > 5):
    print("The number is less than 5")    
else:
    print("I dont KNow what to say")

#Problem 1:

Mark = int(input("Enter your mark: "))
if(Mark >= 35):
    print("Passed")
else:
    print("Failed")

#Problem 2:

Income = int(input("Enter your income: "))
if(Income >= 7000):
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")  

#Problem 3:

number = int(input("Enter a number: "))
if(number % 3 == 0 and number % 5 == 0):
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by both 3 and 5")       

#Problem 4:

number = int(input("Enter a number: "))
if(number % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")

#Problem 5:

score = int(input("Enter your score: "))
if(score < 35):
    print("Poor Student") 
elif(score > 35 and score < 70):
    print("Average Student")
elif(score >= 70 and score <= 100):
    print("Good Student")
else:
    print("Invalid Score or Score is greater than 100")   



email = "ashwin@gmail.com"

email = email.strip()
if email == '':
    print("Email is empty")
elif not( '.' in email and '@' in email):
    print('email must contain . and @')
elif email.count('@') > 1:
    print('email must contain only one @')
elif not email.endswith(('.com', '.org', '.net')):
    print('email must end with .com', '.org', '.net')
elif not len(email) < 255:
    print('email must be less than 254 characters')
elif not( email[0].isalnum() and  email[-1].isalnum()):
    print('email must start and end with alphanumeric characters')
else:
    print('email is valid')

for i in (1,2,3):
    print(i)

for i in range(1,4):
    print(f"Round: {i}")

    
scores = [23, 45, 67, 18]
total = 0
for score in scores:
    total += score
    print("current total", total)
print("Final total", total)    


files = [" Report.csv", "DATA.csv ", " final.txt"]
for file in files:
    file = file.strip().lower().replace('.txt', '.csv' )
    print(f"Processing {file}")

num = 7
i = 0
for i in range(1, 11):
    print(f"{num}*{i} = {num * i}")    

star = "*"
i = 0
for i in range(1,7):
    print(star * i)    


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]   
for day in days:
    if day in ('Saturday', 'Sunday'):
        continue
    else:
        print(f"{day} is a weekday")

emails = ["ashwin@gmail.com", "baara@gmail.com", "DROP YOUR EMAIL"]
for email in emails:
    if '@' in email and email.endswith('.com'):
        print(f"{email} is a valid email")
    else:
        print(f"{email} this is not a email, it contains vulnerable data")          