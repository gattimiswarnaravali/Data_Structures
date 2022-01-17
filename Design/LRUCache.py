class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
        
class LRUCache:
    def _add_node(self, node):        
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node       
        
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
    
    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        
        prev.next = new
        new.prev = prev
        
    def _pop_tail(self):
        rev = self.tail.prev
        self._remove_node(rev)
        return rev
        
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        
        if not node:
            return -1
        self._move_to_head(node)
        
        return node.value
        

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value
            
            self.cache[key] = newNode
            self._add_node(newNode)
            
            self.size += 1
            if self.size > self.capacity:
                end = self._pop_tail()
                del self.cache[end.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)
                

# Your LRUCache object will be instantiated and called as such:
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
capacity,key,value = 2,1,3
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
param_1 = obj.get(1)
obj.put(3,3)
param_1 = obj.get(2)
obj.put(4,4)
param_1 = obj.get(1)
param_1 = obj.get(3)
param_1 = obj.get(4)