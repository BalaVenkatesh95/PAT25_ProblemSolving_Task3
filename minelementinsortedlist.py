'''
Find minimum element in sorted list
'''

'''
Sorting element first makes it easy to find a minimum element
'''
given_list = [2, 4, 5, 8, 1, 5, 8, 10]
#Using Sorted() to sort given list
sorted_list = sorted(given_list)
#As we sorted provided list , value present in first address is minimum value
min_value = sorted_list[0]
#printing given values and output
print("Given List:",given_list)
print("Sorted List:",sorted_list)
print("Minimum Value in List:",min_value)