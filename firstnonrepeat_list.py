'''
Program to find first non-repeating element in given
list of integers
'''
#Declaration of list
given_list = [22,33,45,22,33]
#Declaring empty dictionary to assign count to values
element_count = {}

#Using for loop to iterate
#this for loop helps in getting count of numbers to add into dictionary
for num in given_list[:]:
    if num in element_count:
        element_count[num]+=1
    else:
        element_count[num]=1
'''this for loop takes value and check which value
 has count of 1 in dictionary to confirm on non-repetition
 '''
for num in given_list:
    if element_count[num]==1:
        print("First non-repeating integer:",num)