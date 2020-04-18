#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 14:18:56 2020

@author: fernar1
@desc: Module contains generic decorator functions 
"""

import functools


def is_int(indexes):
    """
    validates all the input specified via indexes is int
    """

    def decorator_is_int(func):
        @functools.wraps(func)
        def wrapper_is_int(*args, **kwargs):
            for index in indexes:
                if type(args[index]) != int:
                    raise ValueError(
                        "Integer input expected for argument:" + str(index)
                    )
            return func(*args, **kwargs)

        return wrapper_is_int

    return decorator_is_int


def is_positive(indexes):
    """
    validates all the input specified via indexes is a positive integer
    """

    def decorator_is_positive(func):
        @functools.wraps(func)
        def wrapper_is_positive(*args, **kwargs):
            for index in indexes:
                if args[index] < 0:
                    raise ValueError(
                        "Positive integer expected for " "parameter:" + str(index)
                    )
            return func(*args, **kwargs)

        return wrapper_is_positive

    return decorator_is_positive


def is_single_alphabet(indexes):
    """
    validates all the input specified via indexes is a single alphabet
    """

    def decorator_is_single_alphabet(func):
        @functools.wraps(func)
        def wrapper_is_single_alphabet(*args, **kwargs):
            for index in indexes:
                if not args[index].isalpha() or len(args[index]) > 1:
                    raise ValueError(
                        "Only a single alphabet expected for " "parameter:" + str(index)
                    )
            return func(*args, **kwargs)

        return wrapper_is_single_alphabet

    return decorator_is_single_alphabet


# -----------------------------------------------------------------------------
def main():
    print("The module cannot be run directly.")
    print("Please import the module to use the module functions.")
    return None


if __name__ == "__main__":
    main()
