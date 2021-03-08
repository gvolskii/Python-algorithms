class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        string_in_bytes = key.encode('utf-8')
        return sum(map(lambda x: (x[0] + 1) * x[1], enumerate(string_in_bytes))) % self.size

    def is_key(self, key):
        return key in self.slots

    def put(self, key, value):
        index = self.hash_fun(key)
        self.slots[index] = key
        self.values[index] = value
        
    def get(self, key):
        if not self.is_key(key):
            return None
        return self.values[self.slots.index(key)]
