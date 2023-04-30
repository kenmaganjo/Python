#Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.

def even_or_odd():
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
number = even_or_odd()



print(number)
