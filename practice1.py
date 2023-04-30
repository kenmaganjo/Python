# a pyramid of stars(*)
for i in range(6):
    for j in range(-7,-i):
        print(" ", end = "")
    for k in range(i + 1):
        print("*", end = " ")
    print()
