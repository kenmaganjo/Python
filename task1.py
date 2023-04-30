#Write a program that prompts the user to enter the base and height of a triangle and returns its area.
def area_of_triangle (b,h):
    area = 1/2 * base * height
    area = round(area,2)

    return area

base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = area_of_triangle(base,height)






print("Area =", area)