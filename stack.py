class Element:
    def __init__(self, value):
        self.value = value
        self.prev = None


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
            self.head = element

        self.length += 1

    def pop(self):
        if self.head is None:
            return None
        else:
            k = self.head
            self.head = self.head.prev
            self.length -= 1
            return k.value

    def top(self):
        if self.length == 0:
            return None
        else:
            return self.head.value

    def size(self):
        return self.length

    def is_empty(self):
        if self.head is not None:
            return False
        else:
            return True

    def clear(self):
        self.head = None
        self.length = 0
