#Define Node Class

class Node:
    
    #Function to initialize the node object
    def __init__(self, data):
        self.data = data 
        self.next = None 
			 


#linked list class
class  LinkedList:

    #function to initialize the linked
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next

#Code execution starts here
if __name__ == '__main__':
	
    #start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    #link first node with second
    llist.head.next = second

    #link second node with the third node
    second.next = third

    llist.printList()

