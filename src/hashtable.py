# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.entries = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        idx = self._hash_mod(key)
        node = LinkedPair(key, value)
        node.next = self.storage[idx]
        self.storage[idx] = node

    def remove(self, key):
        idx = self._hash_mod(key)
        if self.storage[idx] is None:
            return

        current = self.storage[idx]
        if current.key == key:
            self.storage[idx] = current.next
            return

        previous = current
        while current:
            if current.key == key:
                previous.next = current.next
                return

            else:
                previous = current
                current = current.next

    def retrieve(self, key):
        idx = self._hash_mod(key)
        current = self.storage[idx]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def resize(self):
        self.capacity *= 2

        new_table = HashTable(self.capacity)

        for i in self.storage:
            current = i
            while current:
                index = self._hash_mod(current.key)
                new_table.insert(current.key, current.value)
                current = current.next
        self.storage = new_table.storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
