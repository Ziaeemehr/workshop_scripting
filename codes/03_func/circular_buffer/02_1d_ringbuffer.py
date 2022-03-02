#!/usr/bin/env python

import numpy as np


class RingBuffer(object):
    def __init__(self, size_max, default_value=0.0, dtype=float):
        """initialization"""

        self._data = np.empty(size_max, dtype=dtype)
        self._data.fill(default_value)

    def append(self, value):
        """append an element"""
        self._data = np.roll(self._data, -1)
        self._data[-1] = value
    
    def get_all(self):
        """return a list of elements from the oldest to the newest"""
        return(self._data)


if __name__ == "__main__":

    obj = RingBuffer(10, dtype=int)
    for i in range(20):
        obj.append(i)
        print(obj.get_all())
    
    print(type(obj.get_all()))
