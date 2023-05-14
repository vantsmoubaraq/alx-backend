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
        """ get paginated data with a given page and page_size """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        end = min(end, len(self.dataset()))
        if start > len(self.dataset()):
            return []
        return self.__dataset[start:end]
