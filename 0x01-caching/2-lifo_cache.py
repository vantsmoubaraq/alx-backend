#!/usr/bin/env python3

"""
Implements class LIFOCache
"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """Implements FIFO cache"""
    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Assigns value to cache"""
        if key and item:
            self.cache_data[key] = item
            if key in self.stack:
                self.stack.remove(key)
            self.stack.append(key)

        if len(self.stack) > self.MAX_ITEMS:
            popped = self.stack.pop(-2)
            del self.cache_data[popped]
            print(f"DISCARD: {popped}")

    def get(self, key):
        """Returns value"""
        return self.cache_data.get(key)
