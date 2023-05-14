#!/usr/bin/env python3

"""
Return a tuple of size two containing a start index and an end index
"""

import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple:
    """
    Return a tuple of size two containing
    a start index and an end index
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        ind = index_range(page, page_size)

        server = Server()
        data = server.dataset()

        for value in ind:
            if value < 0 or value >= len(data):
                return []

        return data[ind[0]:ind[1]]
