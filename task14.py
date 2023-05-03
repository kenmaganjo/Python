#Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
for i in range(3):
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))
        sum = num1 + num2

        print("Sum =", sum)
        break

            
    except ValueError:
        print("Invalid character entered. Enter numbers or floats only.")



       

