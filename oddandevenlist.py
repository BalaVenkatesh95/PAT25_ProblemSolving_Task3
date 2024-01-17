'''
#Problem1: From given list of numbers,
 create 2 separate list one with odd numbers and one with even numbers
 '''
#Variable Declaration
list_1 = [10,501,22,37,100,999,87,351]
print(list_1)
even_list = []
odd_list = []
#Using for loop to iterate through list
#Note:[:] ensures that each item present in list will be iterated
#append() - to insert value to list
for number in list_1[:]:
    if number % 2==0:
        even_list.append(number)
    else:
        odd_list.append(number)
print("List of even numbers:",even_list)
print("List of odd numbers:",odd_list)





