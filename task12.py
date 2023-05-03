#Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.
def largest_number():   
    if num1 > num2 and num1 > num3 and num1 > num4:
        return num1
    else:
        if num2 > num1 and num2 > num3 and num2 > num4:
            return num2
        else:
            if num3 > num1 and num3 > num2 and num3 > num4:
                return num3
            else:
                return num4

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
num3 = float(input("Enter the 3rd number: "))
num4 = float(input("Enter the 4th number: ")) 

number = largest_number()

# print(number)
