class SAPriorityQueue:
    def __init__(self):
        # array sorted backwards
        self.p_queue = []
    
    def remove_minimum(self):
        if(len(self.p_queue)==0):
            return None

        return self.p_queue.pop()

    def insert(self,x):
        for i in range(len(self.p_queue)):
            if(self.p_queue[i]<x):
                self.p_queue.insert(x,i)
                return
        
        self.p_queue.append(x)

    