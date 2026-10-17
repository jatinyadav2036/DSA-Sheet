
class MyHashMap(object):

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key, value):
        index = key % self.size

        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return

        self.buckets[index].append((key, value))

    def get(self, key):
        index = key % self.size

        for k, v in self.buckets[index]:
            if k == key:
                return v

        return -1

    def remove(self, key):
        index = key % self.size

        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index].pop(i)
                return
