#!/usr/bin/env python3

"""
Implements class LRUCache
"""

import datetime
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """Implements LRU cache"""
    def __init__(self):
        super().__init__()
        self.time_stamp = {}

    def put(self, key, item):
        """Assign value to cache"""
        if key and item:
            self.cache_data[key] = item
            self.time_stamp[key] = datetime.datetime.now()

        if len(self.cache_data) > self.MAX_ITEMS:
            lru = datetime.datetime.now()
            least_key = None
            for key, value in self.time_stamp.items():
                if value < lru:
                    lru = value
                    least_key = key
            del self.time_stamp[least_key]
            del self.cache_data[least_key]
            print(f"DISCARD: {least_key}")

    def get(self, key):
        """Retrieve data from cache"""
        if key in self.cache_data:
            self.time_stamp[key] = datetime.datetime.now()
        return self.cache_data.get(key)
