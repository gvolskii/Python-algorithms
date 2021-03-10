class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        self.bloom_filter = [0] * f_len

    def hash1(self, str1):
        slot = 0
        for c in str1:
            slot = (slot * 17 + ord(c)) % self.filter_len
        return slot

    def hash2(self, str1):
        slot = 0
        for c in str1:
            slot = (slot * 223 + ord(c)) % self.filter_len
        return slot

    def add(self, str1):
        self.bloom_filter[self.hash1(str1)] = self.bloom_filter[self.hash2(str1)] = 1

    def is_value(self, str1):
        return bool(self.bloom_filter[self.hash1(str1)] and self.bloom_filter[self.hash2(str1)])
