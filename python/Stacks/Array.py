class StackArray:
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.append(x)
        
    def pop(self,x):
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def top_element(self):
        return self.stack[-1]