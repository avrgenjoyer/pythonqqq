class stack:
    def __init__(self, A):
        self.A = A
    def push(self, x):
        self.A.append(x)
    def pop(self): 
        return self.A.pop()
    def top(self):    
        return self.A[-1]
    def size(self):    
        return len(self.A)
    def clear(self):   
        if self.A == []:
            return True
        else:
            return False
B=[1,2,3,132]
xstack=stack(B)
print(xstack.X())
        
