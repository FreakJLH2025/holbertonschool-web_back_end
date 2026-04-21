#!/usr/bin/env python3
"""
Module 1-simple_pagination
Defines index_range and Server class for pagination
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indexes for pagination.

    Args:
        page (int): current page number (1-indexed)
        page_size (int): number of items per page

    Returns:
        Tuple[int, int]: (start index, end index)
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
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # skip header
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset.

        Args:
            page (int): page number (must be > 0)
            page_size (int): number of items per page (must be > 0)

        Returns:
            List[List]: list of rows for the requested page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []
        return dataset[start:end]
