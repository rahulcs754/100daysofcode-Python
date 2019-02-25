# Python code to demonstrate the working of 
# typecode, itemsize, buffer_info() 

# importing "array" for array operations 
import array 

# initializing array with array values 
# initializes array with signed integers 
arr= array.array('i',[1, 2, 3, 1, 2, 5]) 

# using typecode to print datatype of array 
print ("The datatype of array is : ",end="") 
print (arr.typecode) 

# using itemsize to print itemsize of array 
print ("The itemsize of array is : ",end="") 
print (arr.itemsize) 

# using buffer_info() to print buffer info. of array 
print ("The buffer info. of array is : ",end="") 
print (arr.buffer_info()) 


# Python code to demonstrate the working of 
# count() and extend() 

# importing "array" for array operations 
import array 

# initializing array 1 with array values 
# initializes array with signed integers 
arr1 = array.array('i',[1, 2, 3, 1, 2, 5]) 

# initializing array 2 with array values 
# initializes array with signed integers 
arr2 = array.array('i',[1, 2, 3]) 

# using count() to count occurrences of 1 in array 
print ("The occurrences of 1 in array is : ",end="") 
print (arr1.count(1)) 

# using extend() to add array 2 elements to array 1 
arr1.extend(arr2) 

print ("The modified array is : ",end="") 
for i in range (0,9): 
	print (arr1[i],end=" ") 


# Python code to demonstrate the working of 
# fromlist() and tolist() 

# importing "array" for array operations 
import array 

# initializing array with array values 
# initializes array with signed integers 
arr = array.array('i',[1, 2, 3, 1, 2, 5]) 

# initializing list 
li = [1, 2, 3] 

# using fromlist() to append list at end of array 
arr.fromlist(li) 

# printing the modified array 
print ("The modified array is : ",end="") 
for i in range (0,9): 
	print (arr[i],end=" ") 

# using tolist() to convert array into list 
li2 = arr.tolist() 

print ("\r") 

# printing the new list 
print ("The new list created is : ",end="") 
for i in range (0,len(li2)): 
	print (li2[i],end=" ") 
