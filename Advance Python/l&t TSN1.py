
list = ['T','S','N']
print(list)
temp = list[0]
list[0] = list[-1]
list[-1] = temp
print(list)
'''
list = [1,2,3,4,5]
print(list)
#Start, *middle, end = list
#list2 = [end, *middle, Start]
# Reverse the string using slicing
# rr = list[::-2]
# print(rr)

reversed_ls = list[::-1]
print(reversed_ls)
#list1 = reversed_str.reverse()
output_ls = reversed_ls[2:5]
#print(type(list))
#print(type(reversed_str))
#print(type(output_str))
print(output_ls)

'''