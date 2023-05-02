# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driv20er one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.
def check_speed():
    if speed < 70:
        return "Ok"
    else:
        
        if demerit_points > 12:
            return "Points:", demerit_points, "License Suspended"

        else:
            return "Points:", demerit_points

speed = int(input("Enter speed: "))  
demerit_points = (speed - 70) // 5 

speed = check_speed()

# print(speed)



    


