#!/usr/bin/env python3
"""   Duck typing the first element   """
from typing import Any, Union, Sequence, Iterable, List, Tuple


# The types of the elements
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """   Safe the first element   """
    if lst:
        return lst[0]
    else:
        return None