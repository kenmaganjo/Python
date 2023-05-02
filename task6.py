#Write a program input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After ,you show them a message , the account is blocked.
for i in range(4):
    password = input("Enter password: ")
    if password == "admin@123":
        print("Access Granted")
        break
    else:
        print("Invalid password, re-enter your password")
   
print("Account blocked!")









        







    


       
