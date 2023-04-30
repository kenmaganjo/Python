#Write a program which accepts email as form input or from terminal. Validate the email by checking if it contains an “@” symbol and “.” symbol. 
def email_validation():

    if email.count("@") == 1 and email.count(".") == 1:
        
        return "Valid email"
    else:
        return "Invalid email"


email = input("Enter your email: ")

email = email_validation()


print(email) 

