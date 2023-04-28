#Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.

for i in range(3):
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if email == 'admin@mail.com' and password == 'Admin@123':
        print("Login is Successful")
        break
    else:
        print("Invalid username or password")
else:
    print("You have been blocked!")
        
        # ans:
        #     Enter your email: admin@mail.com
        #     Enter your password: Admin@123
        #     Login is Successful

        #     Enter your email: admin@mail.com
        #     Enter your password: amin123
        #     Invalid username or password
        #     Enter your email: ken@gmail.com
        #     Enter your password: Admin@123
        #     Invalid username or password
        #     Enter your email: adminn@mail.com
        #     Enter your password: dfgh
        #     Invalid username or password
        #     You have been blocked!
    


        