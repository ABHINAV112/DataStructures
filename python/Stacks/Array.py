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

    def traversal(self,callback):
        for i in self.stack[::-1]:
            callback(i)
    
    def callback(self,x):
        self.represent.append(x)
    
    def __repr__(self):
        self.represent = []
        self.traversal(self.callback)
        result = self.__class__.__name__+"("
        for i,val in enumerate(self.represent):
            result+=" {} ".format(val)
            if(i!=len(self.represent)-1):
                result+="->"
        result+=")"
        return result
