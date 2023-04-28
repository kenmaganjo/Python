#Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
while True:
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))
        sum = num1 + num2
        print("Sum =", sum)
        break

        
    except ValueError:
        print("Invalid character entered. Enter numbers or floats only.")


        # ans:
        #     Enter a number: 12.65
        #     Enter a number: 45
        #     Sum = 57.65

        #     Enter a number: rg
        #     Invalid character entered. Enter numbers or floats only.
        #     Enter a number: 6
        #     Enter a number: #
        #     Invalid character entered. Enter numbers or floats only.
        #     Enter a number: /
        #     Invalid character entered. Enter numbers or floats only.
        #     Enter a number: 

