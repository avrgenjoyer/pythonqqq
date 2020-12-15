class Element:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Stack:

    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        element = Element(value)
        if self.head is None:
            self.head = element
        else:
            element.prev = self.head
            self.head.next = element    
            self.head = element        

        self.length += 1
    
    def pop(self):
        self.length -=1
        if self.head is None:
            return None
        else:
            k = self.head
            self.head = self.head.prev
            return k
    def top(self):
        return self.head.value
    def size(self):
        return self.length
    def is_empty(self):
        if self.length !=0:
            return False
        else:
            return True
    def clear(self):
        while self.head != None:
            self.head = self.head.prev
        self.length = 0
