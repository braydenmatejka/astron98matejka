import numpy as np

def sorting(matrix):
    # sort function takes in an array and sorts the integers along a given axis
    # choose an axis along the columns, ie axis 0
    result = np.sort(matrix, axis = 0)
    return result