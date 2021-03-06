class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        string_in_bytes = value.encode('utf-8')
        return sum(string_in_bytes) % self.size

    def seek_slot(self, value):
        slot_number = self.hash_fun(value)
        if self.slots[slot_number] is None:
            return slot_number
        else:
            for _ in range((self.size // self.step) * self.step):
                slot_number = (slot_number + self.step) % self.size
                if self.slots[slot_number] is None:
                    return slot_number
        return None

    def put(self, value):
        slot_index = self.seek_slot(value)
        if slot_index is not None:
            self.slots[slot_index] = value
        return slot_index

    def find(self, value):
        slot = self.hash_fun(value)
        if self.slots[slot] == value:
            return slot
        else:
            for _ in range(self.size - 1):
                slot = (slot + 1) % self.size
                if self.slots[slot] == value:
                    return slot
        return None
