# Using Python, 

# [ ] print all the numbers from 0 to 10
# for i in range(11):
#     print(i)
    

# [ ] print all the odd numbers from 0 to 3000

# for i in range(3001):
#     if i % 2 !=0:
#         print(i)
        
# [ ] create a function that iterates through each 
#     value in the list and print out each value

# def listPrint():
#     a = [1,2,3,4,5,6]
#     for i in range(len(a)):
#         a[i] = i
#         print(a[i])
         
    

# [ ] create a function that takes a list as an 
#     argument and returns a sum of all of its values

def takesAList(a):
    total = 0
    for item in range(0,len(a)):
        total = total + a[item]
    return total

mycall = takesAList([1,2,4,5,6,3])
print(mycall)
         
    