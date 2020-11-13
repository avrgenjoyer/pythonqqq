class sum():
    def __init__(self, X):
        self.X=X
    def Check(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
        if (self.a+self.b+self.c) == self.X:
            return 1
        else:
            return 0


xsum=sum(int(input()))
print(xsum.Check(int(input()), int(input()), int(input())))




