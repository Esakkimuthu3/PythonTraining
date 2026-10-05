

def write_log(message):
    with open(r"D:\Python Basics\dummy.txt","a") as file:
        file.write(message + "\n")


def is_valid_email(email):
    return "@" in email and "." in email



def clean_and_split_email(email):
    cl_email = email.strip().lower()

    username, domain = cl_email.split("@")

    return {"username":username,"domain": domain}



def process_user_email(email):
    write_log("Start")
    valid_email = is_valid_email(email)
    if not valid_email:
       write_log(f"Invalid Email received: {{email}}")
    else:
       Clean_email = clean_and_split_email(email)
       write_log(f"Processed Email: {Clean_email}")    
    write_log("End")


email = input("Please enter your email address:")
process_user_email(email)