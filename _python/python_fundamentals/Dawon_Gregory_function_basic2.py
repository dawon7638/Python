# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

# def countDown(a):
#     b = []
#     for item in range(a,-1,-1):
#         b.append(item)
#     return b
# createList = countDown(5)
# print(createList)
        
             
# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

# def listof2(a, b):
#     print(a)
#     return b

# ok = listof2(1, 2)
# print(ok)
    
    
# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

# def firstPlusLength():
#     a = [1,2,3,4,5,9]
#     i = a[0] + len(a)
#     return i

# create = firstPlusLength()
# print(create)
            
        
# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def greaterThanSecond(a):
    b = []
    count = 0
    for idx in range(0,len(a)):
        if a[idx] > a[1]:
            b.append(a[idx])
            count = count +1
    print(count)
    return b
whatever = greaterThanSecond([5,2,3,2,1,4])
print(whatever)
        
 

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def thisLength(a,b):
    newList = []
    count = 0
    for item in range(0,len(a)):
        if item = 
        
        newList.append(item)
        print(newList)
        
    return item

myfunc =thisLength(4,7)
print(myfunc)
         
    
    