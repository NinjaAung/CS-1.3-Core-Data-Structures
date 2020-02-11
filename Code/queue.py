#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        self.count = 0
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # Check if empty
        if self.count == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this queue."""
        # Count number of items
        return self.count

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – Why? adding to the end is constant time"""
        # Insert given item
        self.list.append(item)
        self.count += 1

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Return front item, if any
        if self.is_empty() is False:
            return self.list.head.data
        return None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – Why? removing from the front of a linked list is constant time """
        # Remove and return front item, if any
        if self.is_empty() is True:
            raise ValueError
        else:
            data = self.list.head.data
            self.list.delete(data)
            self.count -= 1
            return data


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # Check if empty
        if len(self.list) == 0:
             return True
        return False

    def length(self):
        """Return the number of items in this queue."""
        # Count number of items
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – Why? appending is constant time"""
        # Insert given item
        self.list.append(item)


    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Return front item, if any
        if self.is_empty():
            return None
        return self.list[0]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n-i) – Why? based off of the index to be popped(0) 
        and the number of items"""
        # Remove and return front item, if any
        if self.is_empty():
            raise ValueError
        return self.list.pop(0)

class deque(LinkedQueue):
    def push_front(self, item):
        """Add an item to the front of the queue"""
        self.list.insert_at_index(0, item)

    def push_back(self, item):
        """Add an item to the back of the queue"""
        self.list.append(item)
    
        

# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue
