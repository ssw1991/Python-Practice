"""
Author: Shilo Wilson

File to store utility functions which have no obvious grouping

"""

from functools import wraps
def memoize(fn):
    cache = {}

    @wraps(fn)
    def wrapper(*args, **kwargs):
        """
        Caching **kwargs as tuples so they are hashable
        :param args:
        :param kwargs:
        :return:
        """
        if (args, tuple(kwargs.items())) not in cache:
            cache[(args, tuple(kwargs.items()))] = fn(*args, **kwargs)
        return cache[(args, tuple(kwargs.items()))]
    return wrapper