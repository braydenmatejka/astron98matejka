# defining a function to raise a number to a power

def power(x, y):
    i = 0
    result = 1
    while i < y: # using a while loop to multiply x by itself y times
        result = result * x
        i += 1
    return result