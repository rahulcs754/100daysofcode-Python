# Python program to illustrate 
# while loop 
count = 0
while (count < 3):	 
	count = count + 1
	print("Hello Geek") 


#Python program to illustrate 
# combining else with while 
count = 0
while (count < 3):	 
	count = count + 1
	print("Hello Geek") 
else: 
	print("In Else Block") 


# Python program to illustrate 
# Single statement while block 
count = 0
while (count == 0): print("Hello Geek") 


# Python program to illustrate 
# Iterating over a list 
print("List Iteration") 
l = ["geeks", "for", "geeks"] 
for i in l: 
	print(i) 
	
# Iterating over a tuple (immutable) 
print("\nTuple Iteration") 
t = ("geeks", "for", "geeks") 
for i in t: 
	print(i) 
	
# Iterating over a String 
print("\nString Iteration")	 
s = "Geeks"
for i in s : 
	print(i) 
	
# Iterating over dictionary 
print("\nDictionary Iteration") 
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d : 
	print("%s %d" %(i, d[i])) 


# Python program to illustrate 
# Iterating by index 

list = ["geeks", "for", "geeks"] 
for index in range(len(list)): 
	print(list[index]) 


# Python program to illustrate 
# combining else with for 

list = ["geeks", "for", "geeks"] 
for index in range(len(list)): 
	print(list[index]) 
else: 
	print("Inside Else Block")
