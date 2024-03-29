class Node:
    def __init__(self,x):
        self.next = None
        self.value = x
    
class StackList:
    def __init__(self):
        self.top = None

    def push(self,x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if(self.top==None):
            return None
        del_node = self.top
        self.top = self.top.next
        del_val = del_node.value
        del del_node
        return del_val
    
    def is_empty(self):
        return self.top==None
    
    def return_top(self):
        return self.top.value
    
    def traversal(self,callback):
        itr = self.top
        while(itr!=None):
            callback(itr)
            itr = itr.next
    
    def callback(self,x):
        self.represent.append(x.value)

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

if(__name__=="__main__"):
    currStack = StackList()
    for i in range(5):
        currStack.push(i)

    currStack.traversal(lambda x:print(x.value))


    print(currStack)
        
