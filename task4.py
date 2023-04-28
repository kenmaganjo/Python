#Write a program which accepts email as form input or from terminal. Validate the email by checking if it contains an “@” symbol and “.” symbol. 

email = input("Enter your email: ")
if email.count("@") == 1 and email.count(".") == 1:
    print("Valid email")
else:
    print("Invalid email")

    # ans:
    #     Enter your email: ken@gmail.com
    #     Valid email 

    #     Enter your email: ken@.gmail.com
    #     Invalid email

    #     Enter your email: ken@gm@il.com
    #     Invalid email

