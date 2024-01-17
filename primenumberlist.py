'''
Fina total Count of prime numbers in list and also
create a separate list of prime numbers
'''
#Declaration of List
numbers = [10,501,22,37,100,999,87,351]
print("List to find prime numbers:",numbers)
prime_count = 0
prime_list = []

#Using for loop to iterate through provided list
#Taking a range from 2 to squareroot of value
#Here else is assocaited with for and not with if
for num in numbers[:]:
    if num>1:
        for i in range(2,int(num**0.5)+1)[:]:
            if (num % i)==0:
                break
        else:
            prime_list.append(num)
            prime_count = prime_count+1
print("Total count of Prime Numbers:",prime_count)
print("Prime List:",prime_list)

