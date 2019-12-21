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
