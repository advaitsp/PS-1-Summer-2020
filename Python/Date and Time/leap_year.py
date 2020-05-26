# Python code to demonstrate the working of isleap() 

# importing calendar module for calendar operations 
import calendar 

year = 2017

# calling isleap() method to verify 
val = calendar.isleap(year) 

# checking the condition is True or not 
if val == True: 

	# print 4th month of given leap year 
	calendar.prmonth(year, 4, 2, 1) 

# Returned False, year is not a leap 
else: 
	print("% s is not a leap year" % year) 
