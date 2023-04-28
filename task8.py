# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driv20er one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.

speed = int(input("Enter speed: "))
if speed < 70:
    print("Ok")
else:
    demerit_points = (speed - 70) // 5
    if demerit_points > 12:
        print("Points:", demerit_points)
        print("License Suspended")
    else:
        print("Points:", demerit_points)

        # ans:
        #     Enter speed: 80
        #     Points: 2
        #     Enter speed: 65
        #     Ok
        #     Enter speed: 70
        #     Points: 0
        #     Enter speed: 140
        #     Points: 14
        #     License Suspended
        


