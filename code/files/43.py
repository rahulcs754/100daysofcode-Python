# Python Program for 
# Creation of String 

# Creating a String 
# with single Quotes 
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ") 
print(String1) 

# Creating a String 
# with double Quotes 
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ") 
print(String1) 

# Creating a String 
# with triple Quotes 
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ") 
print(String1) 

# Creating String with triple 
# Quotes allows multiple lines 
String1 = '''Geeks 
			For 
			Life'''
print("\nCreating a multiline String: ") 
print(String1) 


# Python Program to Access 
# characters of String 

String1 = "GeeksForGeeks"
print("Initial String: ") 
print(String1) 

# Printing First character 
print("\nFirst character of String is: ") 
print(String1[0]) 

# Printing Last character 
print("\nLast character of String is: ") 
print(String1[-1]) 

# Printing 3rd to 12th character 
print("\nSlicing characters from 3-12: ") 
print(String1[3:12]) 

# Printing characters between 
# 3rd and 2nd last character 
print("\nSlicing characters between " +
	"3rd and 2nd last character: ") 
print(String1[3:-2]) 


# Python Program to Update 
# character of a String 

String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 

# Updating a character 
# of the String 
String1[2] = 'p'
print("\nUpdating character at 2nd Index: ") 
print(String1) 
