class stack:
    def __init__(self, A):
        self.A = A
    def push(self, x):      #добавляем в конец
        self.A.append(x)
    def pop(self):      #берет последний эелемент (удаляет последний элемент и выдает его)
        return self.A.pop()
    def top(self):      #значение последнего
        return self.A[-1]
    def size(self):     #кол-во элементов    
        return len(self.A)
    def clear(self):        #проверка на пустоту. True - пустой, False - нет.
        if self.A == []:
            return True
        else:
            return False
B=[1,2,43,14,56]       #произвольный массив
xstack=stack(B)
print(xstack.X())       #вместо X подставить нужную функцию
        
