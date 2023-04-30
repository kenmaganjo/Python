#Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three.
def return_largest(a,b,c):
    if num1 > num2 and num1 > num3:
        return num1    
    else:
        if num2 > num1 and num2 > num3:
            return num2      
        else:
            return num3

    
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
num3 = float(input('Enter the third number: '))  

number = return_largest(num1,num2,num3)


print("Largest number =", number)


        