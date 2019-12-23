class Node:
    def __init__(self,x):
        self.value = x
        self.parent = None
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert_node(self,x):
        new_node = Node(x)

        def recurs(node,x):
            pass
    
    def delete_node(self,x):
        pass

    def in_order(self, node, callback):
        if(self.node!=None):
            self.in_order(node.left,callback)
            callback(self.node)
            self.in_order(node.right,callback)

    def post_order(self,node,callback):
        if(self.node!=None):
            self.in_order(node.left,callback)
            self.in_order(node.right,callback)
            callback(self.node)

    
    def pre_order(self,node,callback):
        if(self.node!=None):
            callback(self.node)
            self.in_order(node.left,callback)
            self.in_order(node.right,callback)

