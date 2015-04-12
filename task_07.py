#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module contains functions that adds values and deducts keys from dict."""


def iter_dict_funky_sum(some_dict):
    """Function takes sum of dictionary values, minus sum of keys.
    Args:
        some_dict (dict): Dictionary of keys and values of Intergers.
    Returns:
        running_total (int): Total sum of values minus total sum of keys.

    Examples:
        >>> import task_07
        >>> task_07.iter_dict_funky_sum(task_07.DATA)
        140166242
    """
    running_total = 0
    for keys, values in some_dict.iteritems():
        running_total += values
        running_total -= keys
    return running_total
