#Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
try:
    marks = float(input("Enter student marks: "))
    if marks < 0 or marks > 100:
        print("Inavlid marks")
    else:
        if marks > 79:
            print("Grade: A")
        else:
            if marks >= 60 and marks <= 79:
                print("Grade: B-")
            else:
                if marks >= 49 and marks <= 59:
                    print("Grade: C-")
                else:
                    if marks >= 40 and marks <= 49:
                        print("Grade: D")
                    else:
                        print("Grade: E")
except Exception as x:
    print(x)

    # ans:
    #     Enter student marks: 55
    #     Grade: C-
    #     Enter student marks: 39
    #     Grade: E
    #     Enter student marks: -8
    #     Inavlid marks
    #     Enter student marks: 108
    #     Inavlid marks
