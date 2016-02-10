class Stack:
    def __init__(self):
        self.items = []
        self.top = 0
        
    def isEmpty(self):
        return self.top == 0
    
    def push(self, item):
        self.items.append(item)
        self.top += 1
        
    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Stack Underflow")
        item = self.items[self.top - 1]
        del self.items[self.top - 1]
        self.top -= 1
        return item
    
    def peep(self):
        if self.isEmpty():
            raise RuntimeError("Stack Underflow")
        return self.items[self.top - 1]
    
def main():
    s = Stack()
    lst = list(range(10))
    lst2 = []
    
    for k in lst:
        s.push(k)
        
    if s.peep() == 9:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")
        
    while not s.isEmpty():
        lst2.append(s.pop())
        
    lst2.reverse()
    
    if lst2 != lst:
        print("Test 2 Failed")
    else:
        print("Test 2 Passed")
        
if __name__=="__main__":
    main()