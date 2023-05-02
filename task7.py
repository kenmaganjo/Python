#Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
def marks_grading(): 
    try:
        
        if marks < 0 or marks > 100:
            return "Inavlid marks"
        else:
            if marks > 79:
                return "Grade: A"
            else:
                if marks >= 60 and marks <= 79:
                    return "Grade: B-"
                else:
                    if marks >= 49 and marks <= 59:
                        return "Grade: C-"
                    else:
                        if marks >= 40 and marks < 49:
                            return "Grade: D"
                        else:
                            return "Grade: E"
                            
    except Exception as x:
        return(x)

marks = float(input("Enter student marks: ")) 

marks = marks_grading()

# print(marks)

    
