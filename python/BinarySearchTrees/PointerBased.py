class Node:
    def __init__(self,x):
        self.value = x
        self.parent = None
        self.left = None
        self.right = None
    
    # insert a value
    def insert_value(self,x):
        pass

    # delete a node when given the same node
    def delete_node(self,node):
        pass
    
    # find the value then delete
    def delete_value(self,x):
        pass
    
    def pre_order(self,node,callback):
        if(node!=None):
            callback(node)
            self.pre_order(node.left,callback)
            self.pre_order(node.right,callback)
    
    def post_order(self,node,callback):
        if(node!=None):
            self.pre_order(node.left,callback)
            self.pre_order(node.right,callback)
            callback(node)
    
    def in_order(self,node,callback):
        if(node!=None):
            self.pre_order(node.left,callback)
            callback(node)
            self.pre_order(node.right,callback)

    def find_node(self,x):
        pass
            


