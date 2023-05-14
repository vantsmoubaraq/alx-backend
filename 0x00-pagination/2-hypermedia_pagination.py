#!/usr/bin/env python3
"""
Pagination Module
Server class
"""
import csv
import math
from typing import List, TypedDict, Optional


Hyper = TypedDict('Hyper', {
    "page_size": int,
    "page": int,
    "data": List[List],
    "next_page": Optional[int],
    "prev_page": Optional[int],
    "total_pages": int
})


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Hyper:
        """ Returns details of the pagination """
        data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        end = min(end, len(self.dataset()))
        hypers: Hyper = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if end != len(self.dataset()) else None,
            "prev_page": page - 1 if start != 0 else None,
            "total_pages": math.ceil(len(self.dataset()) / page_size)
        }

        return hypers


def index_range(page: int, page_size: int) -> tuple:
    """ return a start index and an end index corresponding to the range """
    start = sum([page_size for i in range(page - 1)]) if page > 0 else 0
    end = page_size + start
    return (start, end)
