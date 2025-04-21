# Q2 Write a Python Program to do Arithmetical Operation Addition and Division...?
# Addition
num1 = float(input("Enter the First Number for Addition: "))
num2 = float(input("Enter the Second Number for Addition: "))
sum_result = num1 + num2
print(sum_result)
print(f"sum : {num1} + {num2} = {sum_result}")
print(id(num1))
print(id(num2))

# Division

num3 = float(input("Enter the First Number for Division: "))
num4 = float(input("Enter the Second Number for Division: "))
if num4 == 0:
    print("Error: Division by Zero is not allowed.")
else:
    div_result = num1/num2
    print(f"Division : {num3} / {num4} = {div_result}")