# if 5 > 6 or 3 < 1 or 4 < 2:
#     print("True")
#     print("True is displayed")
#     print("display true")

# else:
#     print("False")
#     print("False is diplayed")

# print("Program excuted")
try:
    marks = float(input("Marks: "))
    if marks < 0 or marks > 100:
        print("Invalid marks")
    else:
        if marks >= 70:
            print("A")
        else:
                if marks >= 60 and marks < 70:
                    print("B")
                else:
                        if marks >= 50 and marks < 60:
                            print("C")
                        else:
                                if marks >= 40 and marks < 50:
                                    print("D")
                                else:
                                        print("E")
except Exception as x:
    print(x)







    # if marks >= 70:
    #      print("A")
    #     else:
    #         if marks >= 60 and marks < 70:
    #             print("B")
    #             else:
    #                 if marks >= 50 and marks < 60:
    #                     print("C")
    #                     else:
    #                         if marks >= 40 and marks < 50:
    #                             print("D")
    #                             else:
    #                                 print("E") 










# if marks >= 70:
#     print("A")
# elif marks >= 60 and marks < 70:
#     print("B")
# elif marks >= 50 and marks < 60:
#     print("C")
# elif marks >= 40 and marks < 50:
#     print("D")
# else:
#     print("E")

#Take 3 numbers from a user and return the largest of the 3.

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))
# #solution 1
# if num1 > num2 and num1 > num3:
#     print("num1")
# elif num2 > num1 and num2 > num3:
#     print("num2")
# elif num3 > num1 and num3 > num1:
#     print("num3")
# else:
#     print("num1 = num2 = num3")
# #solution2
# number1 = int(input("Enter 1st number"))
# number2 = int(input("Enter 1st number"))
# number3 = int(input("Enter 1st number"))

