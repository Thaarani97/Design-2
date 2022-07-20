class MyHashMap:
    class Node:
        def __init__(self,key,value):
            self.key = key
            self.val = value
            self.next = None

    def __init__(self):
        self.bucketlen = [None] * 10000 
    
    def hashfunc(self,key):
        return key % len(self.bucketlen)
    
    def find_node(self,head,key):
        curr = head
        prev = None 
        while curr!=None and curr.key!=key:
            prev = curr
            curr = curr.next
        return prev      

    def put(self, key: int, value: int) -> None:
        hashidx = self.hashfunc(key)
        if self.bucketlen[hashidx] == None:
            self.bucketlen[hashidx] = self.Node(-1,-1)
        prev_node = self.find_node(self.bucketlen[hashidx],key)
        if prev_node.next == None:
            prev_node.next = self.Node(key,value)
        else:
            prev_node.next.val = value      

    def get(self, key: int) -> int:
        hashidx = self.hashfunc(key)
        if self.bucketlen[hashidx] == None:
            return -1
        prev_node = self.find_node(self.bucketlen[hashidx],key)
        if prev_node.next == None:
            return -1
        else:
            return prev_node.next.val
            
    def remove(self, key: int) -> None:
        hashidx = self.hashfunc(key)
        if self.bucketlen[hashidx] == None:
            return 
        prev_node = self.find_node(self.bucketlen[hashidx],key)
        if prev_node.next == None:
            return
        prev_node.next = prev_node.next.next
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)