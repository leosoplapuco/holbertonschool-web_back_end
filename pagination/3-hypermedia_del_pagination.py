#!/usr/bin/env python3
"""   Hypermedia del pagination   """

import csv
import math
from typing import List, Dict, Tuple


class Server:
    """   Server class to paginate a database with baby names.   """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None


        return {
            "index": index,
            "next_index": i,
            "page_size": page_size,
            "data": d
        }
