class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        
    def hash_fun(self, key):
        string_in_bytes = key.encode('utf-8')
        return sum(map(lambda x: (x[0] + 1) * x[1], enumerate(string_in_bytes))) % self.size
    
    def is_key(self, key):
        return key in self.slots
    
    def put(self, key, value):
        index = self.hash_fun(key)
        if self.slots[index] is None:
            self.slots[index] = key
            self.values[index] = value
            return
        for _ in range(self.size - 1):
            index = (index + 1) % self.size
            if self.slots[index] is None:
                self.slots[index] = key
                self.values[index] = value
                return
        index = self.hits.index(min(self.hits))
        self.slots[index] = key
        self.values[index] = value
        self.hits[index] = 0
    
    def get(self, key):
        if not self.is_key(key):
            return None
        index_key = self.slots.index(key)
        self.hits[index_key] += 1
        return self.values[index_key]             
