# A C-style way of accessing list elements 
cars = ["Aston", "Audi", "McLaren"] 
i = 0
while (i < len(cars)): 
	print cars[i] 
	i += 1


# Accessing items using for-in loop 

cars = ["Aston", "Audi", "McLaren"] 
for x in cars: 
	print x 


# Accessing items using indexes and for-in 

cars = ["Aston", "Audi", "McLaren"] 
for i in range(len(cars)): 
	print cars[i] 


# Accessing items and indexes enumerate() 

cars = ["Aston" , "Audi", "McLaren "] 
for x in enumerate(cars): 
	print (x[0], x[1]) 


# demonstrating the use of start in enumerate 

cars = ["Aston" , "Audi", "McLaren "] 
for x in enumerate(cars, start=1): 
	print (x[0], x[1]) 


# Two separate lists 
cars = ["Aston", "Audi", "McLaren"] 
accessories = ["GPS kit", "Car repair-tool kit"] 

# Single dictionary holds prices of cars and 
# its accessories. 
# First three items store prices of cars and 
# next two items store prices of accessories. 
prices = {1:"570000$", 2:"68000$", 3:"450000$", 
		4:"8900$", 5:"4500$"} 

# Printing prices of cars 
for index, c in enumerate(cars, start=1): 
	print "Car: %s Price: %s"%(c, prices[index]) 

# Printing prices of accessories 
for index, a in enumerate(accessories,start=1): 
	print ("Accessory: %s Price: %s"\ 
		%(a,prices[index+len(cars)])) 
