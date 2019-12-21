class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap_size = 0
    
    def sift_down(self,index):
        i = index
        while(i<self.heap_size):
            
            if(2*i+1>self.heap_size):
                break
            if(2*i+2>self.heap_size):
                min_index = 2*i+1

            elif(self.heap[2*i+1]<self.heap[2*i+2]):
                min_index = 2*i+1
            else:
                min_index = 2*i+2

            if(self.heap[min_index]>self.heap[i]):
                break
            
            self.heap[min_index],self.heap[i] = self.heap[i],self.heap[min_index]

    def sift_up(self,index):
        i = index
        while(i>=0):
            parent = (i-1)//2
            if(parent<0):
                break
            if(self.heap[parent]<self.heap[i]):
                break
            
            self.heap[parent],self.heap[i] = self.heap[i],self.heap[parent]
            i = parent
    
    def insert(self,new_val):
        self.heap.append(new_val)
        self.heap_size+=1
        self.sift_up(self.heap_size-1)
    
    def delete_minimum(self):
        minimum = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heap_size-=1
        self.sift_down(0)
        return minimum
    
    def delete(self,index):
        deleted_element = self.heap[index]
        parent = (index-1)//2
        self.heap[index] = self.heap[-1]
        self.heap.pop()
        self.heap_size-=1
        if(self.heap[parent]>self.heap[index]):
            self.sift_up(index)
        else:
            self.sift_down(index)
        return deleted_element

if(__name__=="__main__"):
    input_list = list(map(int,input().split()))
    MH = MaxHeap()

    for i in input_list:
        MH.insert(i)

    print(MH.heap)
    MH.delete_minimum()
    print(MH.heap)