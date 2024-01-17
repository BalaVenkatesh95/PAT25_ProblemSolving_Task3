'''
From given list and value , find triplet in list
which sum is equal to value
'''
#Provided values
given_list = [10, 20, 30, 9]
target_value = 59
#Initializing empty list to get triplet values
triplet = []
print("Given List:",given_list)
print("Target Value:",target_value)
#Using sum() to get sum value of list
sum = sum(given_list)
'''
Logic is, if subtraction of particular value from list with total sum 
results in target value then remaining element in list is triplet
'''
#remove() - to remove particular element from list
for data in given_list[:]:
    if sum-data == target_value:
        given_list.remove(data)
print("Triplet:",given_list)

