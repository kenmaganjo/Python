#Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01... Convert the number to start with +254… 
def new_phone_number():
    if phone_number.startswith("+254"):
        new_phone_number = phone_number
    elif phone_number.startswith("0"):
        new_phone_number = "+254" + phone_number[1:]
    elif phone_number.startswith("01"):
        new_phone_number = "+254" + phone_number[1:]
    elif phone_number.startswith("7"):
        new_phone_number = "+254" + phone_number
    elif phone_number.startswith("254"):
        new_phone_number = "+" + phone_number
    else:
        new_phone_number = None 
    
    
    return new_phone_number

phone_number = input("Enter phone number: ")

modified_number = new_phone_number()



print(modified_number)








