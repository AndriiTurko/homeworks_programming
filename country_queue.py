'''CountryQueue ADT'''

from collections import deque


class CountryQueue:
    '''Represents Queue ADT'''
    def __init__(self, country):
        '''Initializes queue head, size and name'''
        self._name = country
        self._qhead = self._qtail = None
        self._size = 0

    def add(self, value, year=None):
        '''Adds value to a queue'''
        new_node = Node(value, year, None)
        if self.is_empty():
            self._qhead = new_node
        else:
            self._qtail.next = new_node
        self._qtail = new_node
        self._size += 1

    def pop(self):
        '''Pops element from stack'''
        assert not self.is_empty(), 'Cannot pop...'
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._size -= 1
        return node.item

    def peek(self):
        '''Returns the peak of the queue'''
        return self._qhead

    def is_empty(self):
        '''Checks whether queue is empty'''
        return self._qhead is None

    def __len__(self):
        '''Returns len of the queue'''
        return self._size


class Node:
    '''Represents Node class'''
    def __init__(self, item, year, next=None):
        '''Initializes item and next'''
        self.year = year
        self.item = item
        self.next = next
