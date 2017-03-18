#!/usr/bin/env python

class Node(object):
    'A class defining a linked list node'
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data = d
# End of Node class definition

class LinkedList(object):
    'A class defining a linked list'
    def __init__(self, r = None):
        self.Root = r
        self.Size = 0
    def det_size(self):
        return self.Size
    def get_root(self):
        return self.Root
    def add(self, d):
        new_node = Node(d, self.Root)
        self.Root = new_node
        self.Size +=1
    def remove(self, d):
        this_node = self.Root
        prev_node = None
        while this_node:
            if this_node.get_data == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.Root = this_node
                self.Size -= 1
                return True # data remove
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False # data not found
    def find(self, d):
        this_node = self.Root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None
    def print_me(self):
        this_node = self.Root
        while this_node:
            print this_node.get_data()
            this_node = this_node.get_next()


    def insert_sorted(self, d):
        this_node = self.Root
        prev_node = None
        while this_node:
            if d > this_node.get_data():
                prev_node = this_node
                this_node = this_node.get_next()
                if this_node.get_next() == None: # Reached the end of the list
                    new_node = Node(d)
                    this_node.set_next(new_node)
                    self.Size += 1
                    return True
            else:
                if prev_node: # Inserting in the middle of the list
                    new_node = Node(d)
                    prev_node.set_next(new_node)
                    new_node.set_next(this_node)
                    self.Size += 1
                    return True
                else:
                    self.add(d) # Adding at the beginning of the list
                    return True





# End of LinkedList class definition

MyList = LinkedList()
MyList.add(8)
MyList.add(7)
MyList.add(6)
MyList.add(4)
MyList.add(3)
MyList.add(2)
MyList.add(1)
print"List size is ", MyList.Size
MyList.insert_sorted(10)
MyList.print_me()
print"List size is ", MyList.Size







