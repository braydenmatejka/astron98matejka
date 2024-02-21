# defining a function that takes an integer as input and
# outputs the sum of its digits as an integer

def sumdigs(n):
    sum = 0
    for i in str(n): # for loop through the integer as a string
        sum += int(i) # turning the ith term back into an integer and adding it to sum
    return sum