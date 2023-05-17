#!/usr/bin/env python3
"""
This module implements a MRU caching algorithm.
"""
from base_caching import BaseCaching


def get_mru_item(mru_dict):
    """
    Get the most recently used item from a dictionary of items.

    Args:
        mru_dict (dict): Dictionary of items to evaluate.

    Returns:
        The key of the most recently used item.
    """
    mru = None
    for key, rank in mru_dict.items():
        if mru is None:
            mru = key
        else:
            mru = key if rank > mru_dict[mru] else mru
    return mru


class MRUCache(BaseCaching):
    """
    This class inherits from BaseCaching and is a caching system.
    """
    def __init__(self):
        super().__init__()
        self.mru_track = dict()
        self.RANK = 0

    def put(self, key, item):
        """
        Inserts a new key-value pair into the cache.

        Args:
            key (str): Key to insert into the cache.
            item (str): Value to insert into the cache.

        Returns:
            Nothing.
        """
        if (key is None) or (item is None):
            return

        key_not_found = key not in self.cache_data
        full_cache = len(self.cache_data) >= self.MAX_ITEMS
        if key_not_found and full_cache:
            mru_key = get_mru_item(self.mru_track)
            try:
                del self.mru_track[mru_key]
                del self.cache_data[mru_key]
            except KeyError:
                raise Exception("Erro while discarding MRU item.")
            print("DISCARD: {}".format(mru_key))

        self.mru_track[key] = self.RANK
        self.cache_data[key] = item
        self.RANK += 1

    def get(self, key):
        """
        Retrieves a key-value pair from the cache.

        Args:
            key (str): Key to retrieve from the cache.

        Returns:
            Value associated with the key, or None if key not found.
        """
        if key is None:
            return None

        if key in self.cache_data:
            self.mru_track[key] = self.RANK
            self.RANK += 1
        return self.cache_data.get(key)
