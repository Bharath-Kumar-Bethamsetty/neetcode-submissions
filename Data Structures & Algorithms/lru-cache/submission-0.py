from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.db = {}
        self.cache = deque([])
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.remove(key)
        self.cache.append(key)
        return self.db[key]

    def put(self, key: int, value: int) -> None:
        if key in self.db:
            self.cache.remove(key)
        elif len(self.db) == self.capacity:
            lru = self.cache.popleft()
            del self.db[lru]
        self.db[key] = value
        self.cache.append(key)
        
        
