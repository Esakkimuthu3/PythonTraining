# Dictionaries

user = {"id":1, "name": "Ashwin" , "age":25, "city":"Paris"}

user_str = {
    k: v.upper()
    for k , v in user.items()
    if isinstance(v,str)
}

print(user_str)

#Function

def clean_name(name, a , b):
    print(name)
    age = a * 5
    return age
age = clean_name("ashwin",5,5)
print(age)

#Stores application log messages in a file whenever an event occurs:

def write_log(message):
    with open(r"D:\Python Basics\dummy.txt","a") as file:
        file.write(message + "\n")

write_log("App Started da parathesi")


#clean an email and return into user and domain:

def clean_and_split_email(email):
    cl_email = email.strip().lower()

    username, domain = cl_email.split("@")

    return {"username":username,"domain": domain}


details = clean_and_split_email("ashwin@gmail.com")
print(details)
   

#check whether the password meets the minimum requirements of 8 characters:


def is_valid_password(password):
    return  len(password) >= 8

print(is_valid_password("1gubjdc5ughbj"))

#check if email has a basic valid format


def is_valid_email(email):
    return "@" in email and "." in email

print(is_valid_email("ashwin@gmail.com"))








