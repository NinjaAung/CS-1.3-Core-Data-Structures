from hashtable import HashTable

class HashSet:
    def __init__(self, elements=None):
        """initialize a new empty set structure, and add each element if a sequence is given"""
        self.ht = HashTable()
        self.size = 0

        if elements is not None:
            for element in elements:
                self.add(element)

    def __contains__(self, element):
        """ Uses the in operator. o(1) time complexity, based off of resizing ht."""
        return self.ht.contains(element)

    def __len__(self):
        """uses the len() method, o(1) time complexity, based off of incrementing size stored in the class"""
        return self.ht.size

    def __iter__(self):
        for key in self.ht.keys():
            yield key

    def size(self):
        """returns the size of the hashtable 
        o(1) time complexity, constant number of calls, uses size attr instantiated in class"""
        return self.ht.size

    def items(self):
        return self.ht.keys()

    def contains(self, element):
        """return a boolean indicating whether element is in this set
        o(1) time complexity based off the load factor and resizing attr of the ht class"""
        return self.ht.contains(element)

    def add(self, element):
        """add element to this set, if not present already
        o(1) based off the resizing and hashing of the ht"""
        if not self.contains(element):
            self.ht.set(element, element)
            self.size += 1
    
    def remove(self, element):
        """remove element from this set, if present, or else raise KeyError
        o(1) based off the resizing ascpect of the ht"""
        if self.contains(element):
            self.ht.delete(element)
            self.size -= 1
        else:
            raise KeyError

    def get(self, element):
        return self.ht.get(element)

    def union(self, other_set):
        """return a new set that is the union of this set and other_set
        o(m) where m is the number of items in the smaller set,
        doesn't add duplicates"""
        if len(self) > len(other_set):
            min_set = other_set
            max_set = self
        else:
            min_set = self
            max_set = other_set

        newSet = max_set

        for item in min_set:
            max_set.add(item)
        return newSet

    def intersection(self, other_set):
        """return a new set that is the intersection of this set and other_set
        o(m) where m is the number of items in the smaller set"""
        if len(self) > len(other_set):
            min_set = other_set
            max_set = self
        else:
            min_set = self
            max_set = other_set

        return HashSet([item for item in min_set if max_set.ht.contains(item)])

    def difference(self, other_set):
        """return a new set that is the difference of this set and other_set
        o(n) where n is the number of items in the set."""
        if len(self) > len(other_set):
            min_set = other_set
            max_set = self
        else:
            min_set = self
            max_set = other_set

        newSet = HashSet()
        for item in min_set:
            if not max_set.contains(item):
                newSet.add(item)

        for item in max_set:
            if not min_set.contains(item):
                newSet.add(item)

        return newSet
    
    def is_subset(self, other_set):
        """return a boolean indicating whether self is a subset of the other set
        o(m) where m is the number of items ni the smaller set.
        o(1) best case if self is larger than the other set."""

        # checks if self is larger than the inputted set. If it is larger return False
        # If it is larger self can not be a subset of the other set
        if self.size < other_set.size:
            return False

        for item in other_set.ht.keys():
            if not self.contains(item):
                return False
        return True