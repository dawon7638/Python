# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

# def biggieSize(a):
#     b = []
#     for idx in range(0,len(a)):
#         if a[idx] >= 0:
#             b.append("big")
#         else:b.append(a[idx])
#     return b
    
# create = biggieSize([-1, 3, 5, -5])
# print(create)
    

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

# def countPos(a):
#     count = 0
#     for idx in range(0,len(a)):
#         if a[idx] >= 1:
#             count += 1
#     a[len(a) - 1]  = count   
#     return a
         
    
# call = (countPos([5,5,-5,4,2,-7,-2]))
# print(call)
            
            

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# def sumTotal(a):
#     total = 0
#     for idx in range(0,len(a)):
#         total += a[idx]
#     return total 
        
        
# yes = sumTotal([6,3,-2])
# print(yes)
        
    


# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

# def avg(a):
#     average = 0
#     total = 0
#     for idx in range(0,len(a)):
#         total += a[idx]
#     average = total / len(a)
        
#     return average
# myfunct = avg([1,2,3,4])
# print(myfunct)
    


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

# def myfunc(a):
#     return len(a)
        
# create = myfunc([37,2,1,-9])
# print(create)
        
         
    

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

# def funcMin(a):
#     minimal = 0
#     if len(a) == 0:
#         return "false"
#     minimal = min(a)
#     return min(a)
            
# hey = funcMin([37,2,1,-9,1])
# print(hey)      
    


# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

# def funcMax(a):
#     minimal = 0
#     if len(a) == 0:
#         return "false"
#     minimal = max(a)
#     return max(a)
            
# hello = funcMax([37,2,1,-9,1])
# print(hello)





# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# def ulti(a):
#     total = 0
#     avgs = 0
#     mins = 0
#     maxs = 0
#     lengths = 0
#     empty_dict = {}
    
#     for idx in range(0,len(a)):
#         if a[idx] > maxs:
#             maxs = a[idx]
#         elif a[idx] < mins:
#             mins = a[idx]
#         total += a[idx]
#         avgs = total/float(len(a))
#         lengths += 1
#     empty_dict ["sumTotal"] = total
#     empty_dict ["average"] = avgs
#     empty_dict ["minimum"] = mins
#     empty_dict ["maximum"] = maxs
#     empty_dict ["length"] = lengths
    
#     return empty_dict
# hey = ulti([37,2,1,-9])
# print(hey)
    

            

            
            
    



# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]


# def revList(a):
#     a.reverse()
   
#     return a 

# hola = revList([37,2,1,-9])
# print(hola)
    