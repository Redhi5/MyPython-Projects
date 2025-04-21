# Q10 Write a Python program to swap two variables without temp variable..?

a = 5
b = 10
# a = int(input("Enter the First Value: "))
# b = int(input("Enter the Second Value: "))
# Swapping without a temporary variable
print("before swapping:")
print("a =" , a)
print("b =" , b)
a , b = b , a
print("After swapping:")
print("a =" , a)
print("b =" , b)