# Area of a Rectangle


def area():
    print("Enter the following values in cm")
    a = int(input("Length: "))
    b = int(input("Width: "))
    return "The area of the rectangle is: " + str(a * b) + " centimeters squared"


print(area())
