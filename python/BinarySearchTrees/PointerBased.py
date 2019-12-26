class Node:
    def __init__(self,x):
        self.value = x
        self.parent = None
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert_node(self.root,node): 
        if root==None: 
            root = node 
        else: 
            if root.val < node.val: 
                if root.right == None: 
                    root.right = node 
                else: 
                    insert(root.right, node) 
            else: 
                if root.left == None: 
                    root.left = node 
                else: 
                    insert(root.left, node)
    
    def delete_node(root, key): 
        if root == None: 
            return root  
        if key < root.key: 
            root.left = deleteNode(root.left, key) 
        elif(key > root.key): 
            root.right = deleteNode(root.right, key) 
        else: 
            if root.left == None : 
                temp = root.right  
                root = None 
                return temp    
            elif root.right == None : 
                temp = root.left  
                root = None
                return temp 
            temp = minValueNode(root.right) 
            root.key = temp.key 
            root.right = deleteNode(root.right , temp.key) 
        return root 

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

