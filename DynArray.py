import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        elif i == self.count:
            self.append(itm)
        else:
            if self.count == self.capacity:
                self.resize(2 * self.capacity)
            new_element = itm
            for k in range(i, self.count):
                last_element = self.array[k]
                self.array[k] = new_element
                new_element = last_element
            self.array[self.count] = new_element
            self.count += 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        new_element = self.array[self.count - 1]
        for k in range(self.count - 1, i, -1):
            last_element = self.array[k - 1]
            self.array[k - 1] = new_element
            new_element = last_element
        self.count -= 1
        if (self.count / self.capacity < 0.5) and self.capacity > 16:
            new_capacity = int(self.capacity / 1.5) if (int(self.capacity / 1.5) > 16) else 16
            self.resize(new_capacity)
