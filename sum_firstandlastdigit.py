'''
Program to find sum of first and last digit
of an integer
'''
#Getting input value from user or in runtime using input
input_number = input("Enter any number:")
#input() - always reads input in String, so we are using int() to convert
#Using address to retrieve digits
first_digit = int(input_number[0])
last_digit = int(input_number[-1])
sum = first_digit+last_digit
print("Sum of first and last digit:",sum)

