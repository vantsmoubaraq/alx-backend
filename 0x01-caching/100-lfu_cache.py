#!/usr/bin/env python3

"""
Implements class LFUCache
"""

import datetime
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Implements LFU cache"""
    def __init__(self):
        super().__init__()
        self.count = {}
        self.time_stamp = {}

    def put(self, key, item):
        """Assign value to cache"""
        if key and item:
            self.cache_data[key] = item
            if key in self.count:
                self.count[key] += 1
            else:
                self.count[key] = 0
            self.time_stamp[key] = datetime.datetime.now()

        if len(self.cache_data) > self.MAX_ITEMS:
            lfu = float('inf')
            count_key = None
            all_keys = []
            for item, value in self.count.items():
                if item != key:
                    all_keys.append(value)
                    if value < lfu:
                        lfu = value
                        count_key = item
            if all_keys.count(lfu) > 1:
                unique_lfu = {}
                lru = datetime.datetime.now()
                least_key = None
                for key, value in self.count.items():
                    if value == lfu:
                        unique_lfu[key] = self.time_stamp[key]
                for key, value in unique_lfu.items():
                    if value < lru:
                        lru = value
                        least_key = key
                del self.time_stamp[least_key]
                del self.count[least_key]
                del self.cache_data[least_key]
                print(f"DISCARD: {least_key}")
            else:
                del self.count[count_key]
                del self.time_stamp[count_key]
                del self.cache_data[count_key]
                print(f"DISCARD: {count_key}")

    def get(self, key):
        """Retrieve data from cache"""
        if key in self.cache_data:
            self.count[key] += 1
            self.time_stamp[key] = datetime.datetime.now()
        return self.cache_data.get(key)
