#way1 
# Python program to print even Numbers in a List 
  
# list of numbers 
list1 = [10, 21, 4, 45, 66, 93] 
  
# using list comprehension 
even_nos = [num for num in list1 if num % 2 == 0] 
  
print("Even numbers in the list: ", even_nos) 


#way2
# Python program to print Even Numbers in a List 
  
# list of numbers 
list1 = [10, 21, 4, 45, 66, 93] 
num = 0
  
# using while loop         
while(num < len(list1)): 
      
    # checking condition 
    if num % 2 == 0: 
       print(list1[num], end = " ") 
      
    # increment num   
    num += 1
