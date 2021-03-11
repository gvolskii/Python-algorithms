class PowerSet:
    def __init__(self):
        self.set = []

    def size(self):
        return len(self.set)

    def put(self, value):
        if not self.get(value):
            self.set.append(value)

    def get(self, value):
        return value in self.set

    def remove(self, value):
        if self.get(value):
            self.set.remove(value)
            return True
        return False

    def intersection(self, set2):
        intersec = PowerSet()
        for element in self.set:
            if set2.get(element):
                intersec.put(element)
        return intersec 

    def union(self, set2):
        union = PowerSet()
        union.set = self.set.copy()
        for element in set2.set:
            if not self.get(element):
                union.put(element)
        return union

    def difference(self, set2):
        difference = PowerSet()
        for element in self.set:
            if not set2.get(element):
                difference.put(element)
        return difference

    def issubset(self, set2):
        if set2.size() > self.size():
            return False
        for element in set2.set:
            if not self.get(element):
                return False
        return True
