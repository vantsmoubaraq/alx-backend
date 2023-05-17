#!/usr/bin/env python3

"""
Implements class MRUCache
"""

import datetime
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """Implements MRU cache"""
    def __init__(self):
        super().__init__()
        self.time_stamp = {}

    def put(self, key, item):
        """Assign value to cache"""
        recent_key = None
        if key and item:
            self.cache_data[key] = item
            recent = self.time_stamp[key] = datetime.datetime.now()
            recent_key = key

        if len(self.cache_data) > self.MAX_ITEMS:
            min_time = datetime.datetime(year=1, month=1, day=1)
            diff = recent - min_time
            second_recent = None
            for key, value in self.time_stamp.items():
                if key == recent_key:
                    continue
                if (recent - value) < diff:
                    diff = recent - value
                    second_recent = key
            del self.time_stamp[second_recent]
            del self.cache_data[second_recent]
            print(f"DISCARD: {second_recent}")

    def get(self, key):
        """Retrieve data from cache"""
        if key in self.cache_data:
            self.time_stamp[key] = datetime.datetime.now()
        return self.cache_data.get(key)
