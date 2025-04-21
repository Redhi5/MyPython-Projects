#Q3 Write a Python program to find the area of a triangle...?
import math
# Input the base and height from the user
base = float(input("Enter the length of the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
# Calculate the area of the triangle
# Formula Area = (1/2) * Base * Height 
area = 0.5 * base * height
# Display the result
print(f"The area of the triangle is: {area}")

########################################
# import math

def triangle_area(a, b, c):
    """Calculates the area of a triangle given its 3 sides using Heron's formula."""

    # Calculate the " semi-perimeter "
    s = (a + b + c) / 2

    # Calculate the " area "
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area

if __name__ == "__main__":
    a = float(input("Enter side 1: "))
    b = float(input("Enter side 2: "))
    c = float(input("Enter side 3: "))

    area = triangle_area(a, b, c)
    print("The area of the triangle is:", area)