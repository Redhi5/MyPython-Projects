# Q17 Write a Python Program to Display the multiplication Table..

num = int(input("Display multiplication table of: "))
# for i in range(1, 11):
#     print(f"{num} X {i} = {num*i}")
for i in range(1, 11):
    # num = num*i
    # print(num)
    print (num, 'x', i, '=', num * i)