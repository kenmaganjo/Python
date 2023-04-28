#Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three.
num1 = float(input('Enter a number: '))
num2 = float(input('Enter a number: '))
num3 = float(input('Enter a number: '))
if num1 > num2 and num1 > num3:
    print("Largest number =", num1)
else:
    if num2 > num1 and num2 > num3:
        print("Largest number =", num2)
    else:
        print("Largest number =", num3)

    # ans:
    #     Enter a number: 123.254
    #     Enter a number: 500
    #     Enter a number: 20254.214

    #     Largest number = 20254.214
    
        
        