class Element:
    def __init__(self, num):
        self.num = num
        self.prev = None
        self.next = None

class Stack:

    def __init__(self):
        self.head = None
        self.tail = None
        self.lent = 0

    def push(self, num):
        element = Element(num)
        if self.head is None:
            self.head = element
        else:
            element.prev = self.head
            self.head.next = element    
            self.head = element        

        if self.tail is None:
            self.tail = element

        self.lent += 1
    
    def pop(self):
        if self.head is None:
            print("Error")
        else:
            self.head = self.head.prev
        self.lent -=1
    def top(self):
        return self.head
    def size(self):
        return self.lent
    def clear(self):
        if self.lent !=0:
            return False
        else:
            return True
            