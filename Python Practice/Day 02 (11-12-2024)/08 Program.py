#Q8 Write a Python program to display calendar..?

import calendar

year = int(input("Enter the Year: "))
month = int(input("Enter the Month: "))

cal = calendar.month(year, month)
print(cal)

# Complete Year Calendar
# import calendar

print ("The calendar of year 2024 is : ") 
print (calendar.calendar(2024)) 
