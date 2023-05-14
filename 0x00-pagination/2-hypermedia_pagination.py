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

        data = self.dataset()

        for value in ind:
            if value < 0 or value >= len(data):
                return []

        return data[ind[0]:ind[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        ind = index_range(page, page_size)

        data = self.dataset()

        total_pages = math.ceil(len(data) / page_size)
        next_page = (page + 1) if page < total_pages else None
        prev_page = (page - 1) if page >= 1 else None
        page_info = {"page_size": page_size, "page": page,
                     "data": self.get_page(page, page_size),
                     "next_page": next_page, "prev_page": prev_page,
                     "total_pages": total_pages}
        return page_info
