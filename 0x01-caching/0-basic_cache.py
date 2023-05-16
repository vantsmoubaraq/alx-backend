#!/usr/bin/python3

"""
Module implements BasicCache
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    Class implements BasicCache
    """
    def put(self, key, item):
        """Method assigns values to cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Method retrieves value from cache"""
        return self.cache_data.get(key)
