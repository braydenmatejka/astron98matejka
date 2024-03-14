import numpy as np

def checkerboard():
    # creates an 8x8 array of zeros
    zeros = np.zeros(shape = (8, 8))

    # starting with the row indexed at 0 then alternating every other row, replaces each
    # entry with a 1 starting at index zero and alternating every other entry
    zeros[::2, ::2] = 1

    # starting with the row indexed at 1 then alternating every other row, replaces each
    # entry with a 1 starting at index 1 and alternating every other entry
    zeros[1::2, 1::2] = 1
    
    return zeros