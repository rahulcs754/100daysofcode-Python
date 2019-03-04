# Python code to demonstrate the working of 
# accumulate() and chain() 

# importing "itertools" for iterator operations 
import itertools 

# importing "operator" for operator operations 
import operator 

# initializing list 1 
li1 = [1, 4, 5, 7] 

# initializing list 2 
li2 = [1, 6, 5, 9] 

# initializing list 3 
li3 = [8, 10, 5, 4] 

# using accumulate() 
# prints the successive summation of elements 
print ("The sum after each iteration is : ",end="") 
print (list(itertools.accumulate(li1))) 

# using accumulate() 
# prints the successive multiplication of elements 
print ("The product after each iteration is : ",end="") 
print (list(itertools.accumulate(li1,operator.mul))) 

# using chain() to print all elements of lists 
print ("All values in mentioned chain are : ",end="") 
print (list(itertools.chain(li1,li2,li3))) 




# Python code to demonstrate the working of 
# chain.from_iterable() and compress() 

# importing "itertools" for iterator operations 
import itertools 

# initializing list 1 
li1 = [1, 4, 5, 7] 

# initializing list 2 
li2 = [1, 6, 5, 9] 

# initializing list 3 
li3 = [8, 10, 5, 4] 

# intializing list of list 
li4 = [li1, li2, li3] 

# using chain.from_iterable() to print all elements of lists 
print ("All values in mentioned chain are : ",end="") 
print (list(itertools.chain.from_iterable(li4))) 

# using compress() selectively print data values 
print ("The compressed values in string are : ",end="") 
print (list(itertools.compress('GEEKSFORGEEKS',[1,0,0,0,0,1,0,0,1,0,0,0,0]))) 

# Python code to demonstrate the working of 
# dropwhile() and filterfalse() 

# importing "itertools" for iterator operations 
import itertools 

# initializing list 
li = [2, 4, 5, 7, 8] 

# using dropwhile() to start displaying after condition is false 
print ("The values after condition returns false : ",end="") 
print (list(itertools.dropwhile(lambda x : x%2==0,li))) 

# using filterfalse() to print false values 
print ("The values that return false to function are : ",end="") 
print (list(itertools.filterfalse(lambda x : x%2==0,li))) 
