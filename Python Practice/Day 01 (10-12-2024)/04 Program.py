# Q4 Write a Python program to swap two variables.

# Input two variables
a = int(input("Enter the value of the first variable (a): "))
b = int(input("Enter the value of the second variable (b): "))
# Display the original values
print(f"Original values: a = {a}, b = {b}")
# Swap the values using a temporary variable
temp = a
a = b
b = temp
# Display the swapped values
print(f"Swapped values: a = {a}, b ={b}")