from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# LRU Cache using deque and hasmap TC: O(1), SC: O(capacity)


class LRUCache:

    def __init__(self, capacity: int):
        self._max_size = capacity
        self._dq = deque()
        self._hash_map = {}
        

    def get(self, key: int) -> int:
        if key not in self._hash_map:
            return -1
        self._dq.remove(key)
        self._dq.insert(0, key)
        return self._hash_map[key]
        

    def put(self, key: int, value: int) -> None:
        if key not in self._hash_map:
            if len(self._dq) == self._max_size:
                last_elem = self._dq.pop()
                del self._hash_map[last_elem]
        else:
            self._dq.remove(key)
            del self._hash_map[key]
        
        self._hash_map[key] = value
        self._dq.insert(0, key)