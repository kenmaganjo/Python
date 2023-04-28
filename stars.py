#Write a program called stars.py. It should prompt the user for a number, and it should print the number of stars till the number entered.
num = int(input("Enetr a number: "))
for i in range(num +1):
   print("*" * i)