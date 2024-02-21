# defining a function that takes an input of an integer n and
# returns an integer with its digits to the right one position

def rotdig(n):
    firstdig = n % 10 # the first digit in our result
    lastdigs = n // 10 # the last digits in our result
    i = 1
    magnitude = 0
    while i > 0:
        if n / (10**i) < 1: # using this infinite loop to find the order of magnitude of the integer
            magnitude = 10**(i-1)
            i = -1 # ends the loop with the found magnitude
        else:
            i += 1
    result = lastdigs + (firstdig * magnitude) # multiplying the first digit by that magnitude
    return result