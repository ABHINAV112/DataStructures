class Node:
    def __init__(self , x):
        self.front = None
        self.back = None
        self.value = x

class QueueList:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,x):
        new_node = Node(x)

        if(self.rear == None):
            self.front = new_node
            self.rear = new_node

        else:
            self.rear.back = new_node
            new_node.front = self.rear
            self.rear = new_node
    
    def dequeue(self):
        if(self.front == None):
            return None

        del_node = self.front
        if(del_node.back!=None):
            del_node.back.front = None
        else:
            self.rear = None
        del_val = del_node.value
        self.front = self.front.back
        del del_node
        return del_val

    def is_empty(self):
        return self.rear == None

    def traverse_front_back(self,callback):
        itr = self.front
        while(itr!=None):
            callback(itr)
            itr = itr.back
    
    def traverse_back_front(self,callback):
        itr = self.rear
        while(itr!=None):
            callback(itr)
            itr = itr.front

if(__name__=="__main__"):
    QL = QueueList()
    for i in range(5):
        QL.enqueue(int(input()))
    summ = 0
    def add(x):
        global summ
        summ+=x.value

    QL.traverse_back_front(add)

    print(summ)
    print_val = lambda x:print(x.value)

    QL.traverse_front_back(print_val)