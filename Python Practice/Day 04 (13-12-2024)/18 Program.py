#Q18 Write a Python Program to Print the Fibonacci sequence.
'''
Fibonacci sequence:

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
typically starting with 0 and 1. So, the sequence begins with 0 and 1, 
andthe next number is obtained by adding the previous two numbers.
This pattern continues indefinitely, generating a sequence that looks like this:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
Mathematically, the Fibonacci sequence can be defined using the following 
recurrencerelation:
F(0) = 0 F(1) = 1 F(n) = F(n - 1) + F(n - 2)forn > 1 

'''

'''

nterms = int(input("How many terms?: "))
# first two terms
n1 , n2 = 0 , 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
# generate fibonacci sequence
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
    # update values
        n1 = n2
        n2 = nth
        count += 1
        
'''
'''
# Ans2:
# Fibonacci Numbers using Native Approach..
# We are useing While Loop:
# We are using a while loop to generate the Fibonacci sequence. The loop will continue until the count
# is less than the number of terms. Inside the loop, we print the first number in the
# sequence (n1), then calculate the next number in the sequence (nth) by adding the
# last two numbers (n1 and n2). We then update the values of n1 and
# n2 to be the last two numbers in the sequence. Finally, we increment the count by
# 1. This process continues until the count is less than the number of terms.
n = int(input("Enter The Number: "))
num1 = 0
num2 = 1
next_number = num2  
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()

'''

#Python Program for Fibonacci numbers using Recursion..
# We are using Recursion to generate the Fibonacci sequence. The function will call itself
# until the count is less than the number of terms. Inside the function, we print the first
# number in the sequence (n1), then calculate the next number in the sequence (nth)
# by adding the last two numbers (n1 and n2). We then update the values of
# n1 and n2 to be the last two numbers in the sequence. Finally, we increment
# the count by 1. This process continues until the count is less than the number of terms
def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    '''
    # We are using Recursion to generate the Fibonacci sequence. The function will call itself
    # until the count is less than the number of terms. Inside the function, we print the
    # first number in the sequence (n1), then calculate the next number in the sequence (
        # nth) by adding the last two numbers (n1 and n2). We then update
        # the values of n1 and n2 to be the last two numbers in the sequence.
        # Finally, we increment the count by 1. This process continues until the count is less
        # than the number of terms
        n = int(input("Enter The Number: "))
        num1 = 0
        num2 = 1
        count = 1
        while count <= n:
        print(fibonacci(count), end=" ")
        count += 1
        print()'''
# Test the function
print(fibonacci(9))
        