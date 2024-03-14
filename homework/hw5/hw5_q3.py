import numpy as np

def spaceBetween(array):
    # found this nice numpy function that literally does exactly what i want
    result = np.char.join(" ", array)
    return result