import numpy as np

def findEqual(array):
    # finds the rows (labled i) in the given array in which all the elements in the row are equal.
    # making use of the np.all function that requires a condition and outputs a boolean
    # if the condition is met for all elements in the array
    equalrows = [i for i in array if np.all(i == i[0])]
    return np.array(equalrows)