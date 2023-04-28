# days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
# print(days[2])
# print(len(days))
# days = list(days)
# days[3] = "Thur"
# days = tuple(days)

# print(days)

#A program to calculate the some of numbers
total = 0
i = int(input("Enter a number: "))
# add numbers until the number added is 0
# When the user enters zero, the test condition evaluates to False and the loop ends.
while i != 0:
    total += i
# enter a number again
    i = int(input("Enter a number: "))
print("Total =", total)


