# a = [1,2,3,4,5]

# for i in a:
#     # print(i, end= ",")
#     print(i)

for i in range(1,6):
    for j in range(1,i+1):
        # print(i,j)
        print('* ',end='')
    # print('\r')  # \r is a carriage return, it moves the cursor to the
    # print('* '*i)  # prints numbers from 1 to 9
    print()