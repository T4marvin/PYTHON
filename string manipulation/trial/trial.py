# Program to greet the user by name and ask for their favorite color
name = input("What is your name? ")
color = input("Hi, " + name + "! What is your favorite color? ")
print("Nice! " + color + " is a great color.")

#number 2
# Program to calculate the area of a rectangle or circle
shape = print(len(input("Choose a shape (rectangle/circle): ").lower()))
if shape == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = length * width
    print("The area of the rectangle is:", area)
elif shape == "circle":
    radius = float(input("Enter the radius: "))
    area = 3.14159 * radius ** 2
    print("The area of the circle is:", area)
else:
    print("Invalid shape selected.")
