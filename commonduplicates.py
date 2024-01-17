'''
Find common duplicates of given
3 lists
'''
#List Declaration
given_list1 = [11, 22, 44, 77, 55]
given_list2 = [33, 44, 55, 77, 88]
given_list3 = [44, 77, 55, 25, 65]
#Set intersection is concept which helps us to find common elements of multiple lists
duplicates_in_common = set(given_list1) & set(given_list2) & set(given_list3)
print("Given List01:",given_list1)
print("Given List02:",given_list2)
print("Given List03:",given_list3)
print("Duplicate List with common value:",list(duplicates_in_common))