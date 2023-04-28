from datetime import datetime
mydob = (input("Enter DOB(dd-mm-yyyy): ").split("-"))

mydobnew = []
for i in mydob:
    mydobnew.append(int(i))

mydob = mydobnew
# Validate someone born tomorrow
if len(mydob) != 3 or mydob[0] > 31 or mydob[0] < 1\
or mydob[1] < 1 or mydob[1] > 12 or mydob[2] > 2023\
or len(str(mydob[2])) != 4 or (mydob[1] == 2 and mydob[0] > 29 )\
or (mydob[1] == 2 and mydob[0] > 28 and mydob[2] % 4 != 0)\
or (mydob[1] % 2 == 0 and mydob[0] > 30 and mydob[1] < 8)\
or (mydob[1] % 2 != 0 and mydob[0] > 30 and mydob[1] < 7):
    print("Invalid date")
else:
    print(mydob)
    
