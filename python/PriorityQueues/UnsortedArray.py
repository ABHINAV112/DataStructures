class UAPriorityQueue:
    def __init__(self):
        self.p_queue = []
    
    def remove_minimum(self):
        if(len(self.p_queue)==0):
            return None

        minimum = self.p_queue[0]
        min_index = 0
        for i,val in enumerate(self.p_queue):
            if(val<minimum):
                minimum = val
                min_index = i
        
        return self.p_queue.pop(i)

    def insert(self,val):
        self.p_queue.append(val)
