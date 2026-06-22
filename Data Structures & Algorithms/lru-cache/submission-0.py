class ListNode:

    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
            self.capacity = capacity
            self.hashmap = {}
            self.left = ListNode(0,0)
            self.right = ListNode(0,0)
            self.left.next = self.right
            self.right.prev = self.left
    
    def remove(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self,node):
        prev = self.right.prev
        nxt = self.right
        node.next = nxt
        node.prev = prev
        prev.next =  node
        nxt.prev = node

    def get(self, key: int) -> int:
            if key in self.hashmap:
                self.remove(self.hashmap[key])
                self.insert(self.hashmap[key])
                return self.hashmap[key].val
            return -1


    def put(self, key: int, value: int) -> None:
            if key in self.hashmap:
                self.remove(self.hashmap[key])
            self.hashmap[key] = ListNode(key,value)
            self.insert(self.hashmap[key])
            if len(self.hashmap)>self.capacity:
                lru = self.left.next
                self.remove(lru)
                del self.hashmap[lru.key]


        
