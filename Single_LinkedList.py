

# A class to create a Node.


class Node:

    # __init__ is not a constructor in python. But it is similar to constructor but to only initialise the variables in
    # in the Object. By definition of constructor, object needs to be created by it. But object creation is done by __new__.
    # Use __new__ when you need to control the creation of a new instance.
    # Use __init__ when you need to control initialization of a new instance.
    # __new__ is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
    # In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created.
    #
    # In general, you shouldn't need to override __new__ unless you're subclassing an immutable type like str, int, unicode or tuple.

    # Single Linked List Node contains the data and a pointer to the next Node

    def __init__(self):
        self.next=None
        self.data=None

    # Method to set value of the Node.
    def set_data(self,data):
        self.data  = data

    # Method to get value of the Node.
    def get_data(self):
        return self.data

    # Method to set next Node.
    def set_next(self,next):
        self.next = next

    # Method to get next Node.
    def get_next(self):
        return self.next

    # Method to check if next node exists.
    def has_next(self):
        return self.next!=None


#A class create the Linked List data structure

class Linkedlist:

# Initialise head of the Linked List as None i.e 0 Nodes , empty Linked List
    def __init__(self):
        self.head = None

# Method to Insert Node at the Beginning
    def insert_node_beginning(self,data):
        new_node = Node()
        new_node.set_data(data)

        if self.head !=None:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            self.head = new_node
# Method to insert node at a position
    def insert_node_at_position(self,position,data):
        count = 0
        new_node = Node()
        new_node.set_data(data)
        current = self.head
        if position < self.length and count < position:
            prev = current
            current = current.get_next()
            count += 1
        prev.set_next(new_node)
        new_node.set_next(current)
        self.length+=1
#Method to insert node at the end
    def insert_node_at_end(self,data):
        new_node = Node()
        new_node.set_data(data)
        count = 0
        current = self.head
        while current.has_next()!=False:
            count +=  1
            current = current.get_next()
        current.set_next(new_node)
        self.length += 1
        print(self.length)

#Method to traverse the Linked List and find the Linked List Length
    def traverse_and_singlell_length(self):
        current = self.head
        self.length = 0
        while current.has_next():
            print(current.get_data())

            self.length += 1
            current = current.get_next()
        print(current.get_data())
        print(self.length)


if __name__ == "__main__":

    new_ll = Linkedlist()
    new_ll.insert_node_beginning(5)
    new_ll.insert_node_beginning(3)
    new_ll.insert_node_beginning(11)

    new_ll.traverse_and_singlell_length()
    new_ll.insert_node_at_position(1,9)
    new_ll.traverse_and_singlell_length()
    new_ll.insert_node_at_end(20)
    new_ll.traverse_and_singlell_length()