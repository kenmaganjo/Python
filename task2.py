#Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
num = int(input("Enter a number: "))
if num%2 == 0:
    print("Even")
else:
    print("Odd")

    # ans: 
    #     Enter a number: 7
    #     Odd
    #     Enter a number: 28
    #     Even
    