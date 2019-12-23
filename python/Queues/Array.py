class arrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self,x):
        self.queue.append(x)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def front_val(self):
        return self.queue[0]
    
    def rear_val(self):
        return self.queue[-1]

    def traversal(self,callback):
        for i in self.queue:
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
