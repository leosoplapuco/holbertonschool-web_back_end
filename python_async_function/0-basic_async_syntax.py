#!/usr/bin/env python3
"""
Basic Async Syntax
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:

    """   function async wait_random   """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
