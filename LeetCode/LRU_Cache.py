'''
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Since it’s a cache you need to guarantee a O(1) for reading and writing. For a fast access, hash tables are very often the right data structure so we can consider it, but we need to keep the order and hash tables cannot do that.
An LRU cache is also a FIFO (First In First Out) data structure, a queue looks very adapted too but we loose the O(1) access time.

A good approach is to use both:

An hash table for the O(1) lookup time
A queue to keep the order
The only one problem is that queues are very effective for enqueue and dequeue but very slow for random access, and since each hit has to reorder the queue, those operations would lead to a O(n) lookup time for rearranging the queue every time we access the cache.

The good strategy is to keep this approach but use a double linked list instead of a queue because:

Very easy to implement a queue with it
Still slow for random access but easy to move a given node to the head and it’s all we need

Typically LRU cache is implemented using a doubly linked list and a hash map.
Doubly Linked List is used to store list of pages with most recently used page at the start of the list. So, as more pages are added to the list, least recently used pages are moved to the end of the list with page at tail being the least recently used page in the list.
Hash Map (key: page number, value: page) is used for O(1) access to pages in cache

When a page is accessed, there can be 2 cases:
1. Page is present in the cache - If the page is already present in the cache, we move the page to the start of the list.
2. Page is not present in the cache - If the page is not present in the cache, we add the page to the list.
How to add a page to the list:
   a. If the cache is not full, add the new page to the start of the list.
   b. If the cache is full, remove the last node of the linked list and move the new page to the start of the list.
'''
import collections

class LRUCache:
    # @param  capacity, an integer
    def __init__(self,capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    #get(key) - Get the value (will always be positive) of the key if
    #the key exists in the cache, otherwise return -1. set(key, value) - Set or insert
    #the value if the key is not already present.
    #When the cache reached its capacity, it should invalidate the least
    # recently used item before inserting a new item.
    #return an integer
    def get(self,key):
        val = -1
        if key in self.cache:
            val = self.cache[key]
            del self.cache[key]
            self.cache[key] = val
        return val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            del self.cache[key]
        else:
            if len(self.cache)==self.capacity:
                for keyTemp in self.cache:
                    del self.cache[keyTemp]
                    break
        self.cache[key] = value


import collections

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value
    