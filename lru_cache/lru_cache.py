from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of 
    (1) the max number of nodes it can hold, 
    (2) the current number of nodes it is holding, 
    (3) a doubly-linked list that holds the key-value entries in the correct order, as well as 
    (4) a storage dict that provides fast access to every node stored in the cache.
    """

    def __init__(self, limit=10):
        # 1
        self.max_nodes_num = limit
        # 2
        self.current_nodes_num = 0
        # 3
        self.order = DoublyLinkedList()
        # 4
        self.cache = {}

    """
    (1) Retrieves the value associated with the given key. Also needs to 
    (1a) move the key-value pair to the front of the order such that the pair is considered most-recently used.
    (2) Returns the value associated with the key or 
    (2a) None if the key-value pair doesn't exist in the cache. 
    """

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.order.move_to_front(node)
            return node.value[1]
        else:
            return None
    """
    (1) Adds the given key-value pair to the cache. 
    (1a) The newly-added pair should be considered the most-recently used entry in the cache. 
    (2) If the cache is already at max capacity before this entry is added, 
    (2a) then the oldest entry in the cache needs to be removed to make room. 
    (3) Additionally, in the case that the key already exists in the cache, 
    (3a) we simply want to overwrite the old value associated with the key with the newly-specified value. 
    """

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = (key, value)
            self.order.move_to_front(node)
            return

        if self.current_nodes_num == self.max_nodes_num:
            del self.cache[self.order.tail.value[0]]
            self.order.remove_from_tail()
            self.current_nodes_num -= 1

        self.order.add_to_head((key, value))
        self.cache[key] = self.order.head
        self.current_nodes_num += 1
