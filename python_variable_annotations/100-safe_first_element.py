#!/usr/bin/env python3
""" Return first element of the list """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ function safe_first_element """
    if lst:
        return lst[0]
    else:
        return None
