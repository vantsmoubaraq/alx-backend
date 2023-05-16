#!/usr/bin/env python3

"""
Implements class FIFOCache
"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """Implements FIFO cache"""
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Assigns value to cache"""
        if key and item:
            self.cache_data[key] = item
            if key not in self.queue:
                self.queue.append(key)

        if len(self.queue) > self.MAX_ITEMS:
            popped = self.queue.pop(0)
            del self.cache_data[popped]
            print(f"DISCARD: {popped}")

    def get(self, key):
        """Returns value"""
        return self.cache_data.get(key)
