#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # implement linear search recursively here
    if index > len(array)-1:
        return None
    if item != array[index]:
        return linear_search_recursive(array, item, index+1)
    else:
        return index
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # implement binary search iteratively here
    left_most_index = 0
    right_most_index = len(array) - 1
    while right_most_index >= left_most_index:
        mid_i = int((left_most_index + right_most_index)/2)
        if item == array[mid_i]:
            return mid_i
        elif item > array[mid_i]:
            left_most_index = mid_i + 1
        else:
            right_most_index = mid_i - 1
    return None


def binary_search_recursive(array, item, left=None, right=None):
    # implement binary search recursively here
    if left is None:
        left = 0
        right = len(array) - 1
    mid_i = (left + right) // 2

    if left > right:
        return None
    if item == array[mid_i]:
        return mid_i
    elif item < array[mid_i]:
        right = mid_i - 1
        return binary_search_recursive(array, item, left, right)
    elif item > array[mid_i]:
        left = mid_i + 1
        return binary_search_recursive(array, item, left, right)
