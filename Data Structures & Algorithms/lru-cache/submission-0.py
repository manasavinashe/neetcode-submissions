class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.cap = capacity
        self.left , self.right = Node(0,0) , Node(0,0)
        self.left.next , self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.hashmap :
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        return -1
    def insert ( self, node) : 
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node 
        node.prev, node.next = prev, nxt 

    def remove ( self , node ): 
        prev, nxt =  node.prev , node.next
        prev.next = nxt 
        nxt.prev = prev 

    
    def put(self, key: int, value: int) -> None : 

        if key in self.hashmap :
            self.remove(self.hashmap[key]) # LRU 
            self.hashmap[key] = Node( key, value)
            self.insert(self.hashmap[key]) # MRU
        else : 
            self.hashmap[key] = Node(key, value)
            self.insert(self.hashmap[key])
        
        if len(self.hashmap) > self.cap : 
            lru = self.left.next
            self.remove(lru)
            del self.hashmap[lru.key]


        
