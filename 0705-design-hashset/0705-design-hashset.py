class MyHashSet(object):

    def __init__(self):
        # Choose a prime number for the number of buckets to reduce collisions
        self.num_buckets = 1009
        self.buckets = [[] for _ in range(self.num_buckets)]

    def _hash(self, key):
        # Helper function to calculate the bucket index
        return key % self.num_buckets

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket_idx = self._hash(key)
        if key not in self.buckets[bucket_idx]:
            self.buckets[bucket_idx].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket_idx = self._hash(key)
        if key in self.buckets[bucket_idx]:
            self.buckets[bucket_idx].remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        bucket_idx = self._hash(key)
        return key in self.buckets[bucket_idx]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
