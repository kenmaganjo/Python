#Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01... Convert the number to start with +254… 
phone_number = (input("Enter your phone number: "))
remove_zero = phone_number[1:10]
# prefix_to_add = input("Enter the prefix: ")
prefix_to_add = '+254'
new_phone_number = prefix_to_add + remove_zero
new_phone_number = int(new_phone_number)
print(new_phone_number)
print(type(new_phone_number))

# ans:
#     Enter your phone number: 0727074162
#     254727074162 
#     <class 'int'>



