# Python code to illustrate generator, yield() and next(). 
def generator(): 
	t = 1
	print 'First result is ',t 
	yield t 

	t += 1
	print 'Second result is ',t 
	yield t 

	t += 1
	print 'Third result is ',t 
	yield t 

call = generator() 
next(call) 
next(call) 
next(call) 


# Python code to illustrate generator expression 
generator = (num ** 2 for num in range(10)) 
for num in generator: 
	print(num) 


string = 'geek'
li = list(string[i] for i in range(len(string)-1, -1, -1)) 
print(li) 
