from hashtable import HashTable

class HashSet:
    def __init__(self, elements=None):
        """initialize a new empty set structure, and add each element if a sequence is given"""
        self.ht = HashTable()

        if elements is not None:
            for element in elements:
                self.ht.set(element, None)

    def size(self):
        return self.ht.size

    def contains(self, element):
        """return a boolean indicating whether element is in this set"""
        return self.ht.contains(element)

    def add(self, element):
        """add element to this set, if not present already"""
        if not self.contains(element):
            self.ht.set(element, None)
    
    def remove(self, element):
        """remove element from this set, if present, or else raise KeyError"""
        if not self.contains(element):
            self.ht.delete(element)

    def union(self, other_set):
        """return a new set that is the union of this set and other_set"""

        return HashSet(self.ht.keys() + other_set.hash.keys())

    def intersection(self, other_set):
        """return a new set that is the intersection of this set and other_set"""

        return HashSet([item for item in self.ht.keys() if other_set.hash.contains(item)])

    def difference(self, other_set):
        """return a new set that is the difference of this set and other_set"""

        return HashSet([item for item in self.ht.keys() if not other_set.hash.contains(item)])
    
    def is_subset(self, other_set):
        """return a boolean indicating whether other_set is a subset of this set"""

        # checks if self is larger than the inputted set. If it is larger return False
        # If it is larger self can not be a subset of the other set
        if self.size() > other_set.size():
            return False

        for item in self.ht.keys():
            if not other_set.contains(item):
                return False
        return True