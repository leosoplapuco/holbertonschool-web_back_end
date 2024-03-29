#!/usr/bin/env python3
"""   Hypermdia del pagination   """
import csv
import math
from typing import List, Dict


class Server:
    """   Server class to paginate a database with popular baby names   """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """   function dataset   """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """   function indexed_dataset   """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """   function get_hyper_index   """
        assert type(index) == int and type(page_size) == int
        assert 0 <= index < len(self.dataset())
        dataset = self.indexed_dataset()
        data = []
        next_index = index
        for _ in range(page_size):
            while not dataset.get(next_index):
                next_index += 1
            data.append(dataset.get(next_index))
            next_index += 1
        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data,
        }
