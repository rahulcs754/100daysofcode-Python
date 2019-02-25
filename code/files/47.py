# This function uses global variable s 
def f(): 
	print s 

# Global scope 
s = "I love Geeksforgeeks"
f() 

# This function has a variable with 
# name same as s. 
def f(): 
	s = "Me too."
	print s 

# Global scope 
s = "I love Geeksforgeeks"
f() 
print s 


def f(): 
	print s 

	# This program will NOT show error 
	# if we comment below line. 
	s = "Me too."

	print s 

# Global scope 
s = "I love Geeksforgeeks"
f() 
print s 


# This function modifies global variable 's' 
def f(): 
	global s 
	print s 
	s = "Look for Geeksforgeeks Python Section"
	print s 

# Global Scope 
s = "Python is great!"
f() 
print s 


a = 1

# Uses global because there is no local 'a' 
def f(): 
	print 'Inside f() : ', a 

# Variable 'a' is redefined as a local 
def g():	 
	a = 2
	print 'Inside g() : ',a 

# Uses global keyword to modify global 'a' 
def h():	 
	global a 
	a = 3
	print 'Inside h() : ',a 

# Global scope 
print 'global : ',a 
f() 
print 'global : ',a 
g() 
print 'global : ',a 
h() 
print 'global : ',a 
