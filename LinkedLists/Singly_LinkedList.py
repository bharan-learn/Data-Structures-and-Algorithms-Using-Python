




class Node:

    # Constructor which initialises both value and next value to None

    def __init__(self):
        self.data = None
        self.next = None

    #Method to set value of the Node
    def set_value(self,data):
        self.data = data

    #Method to get value of the Node
    def get_value(self):
        return self.data

    #Method to set next value of the Node

    def set_next(self,next):
        self.next = next

    #Method to get next value of the Node
    def get_next(self):
        return self.next

    #Method to check if there is a next value to the Node
    def has_next(self):
        return self.next!=None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node_beginning(self,data):
        newnode = Node()
        newnode.set_value(data)
        newnode.next = self.head

    def insert_node_at_position(self,prevnode,data):
        newnode = Node()
        newnode.set_value(data)
        newnode.next = prevnode.next
        prevnode.next = newnode

    def insert_node_at_end(self):


    i