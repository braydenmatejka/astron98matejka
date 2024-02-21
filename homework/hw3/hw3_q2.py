# defining a function that takes an input of a list of values and
# returns a tuple with the minimum and maximum list values in that order

def minmax(list):
    min = 0
    count = 0
    for i in list:
        for j in list: # creating a nested for loop to compare the ith term to the jth term
            if i <= j: # testing if the ith term is less than/equal to the jth
                count += 1
            else: # if there is a failure, break the loop and restart the count
                count = 0
                break
            if count == len(list): # has the ith term succeeded in comparison?
                min = i # if so, then the ith term is the minimum value
                break
    max = 0
    count = 0
    for i in list:
        for j in list:
            if i >= j: # does the same thing but tests if the ith term is greater than/equal to the jth
                count += 1
            else:
                count = 0
                break
            if count == len(list):
                max = i
                break
    result = (min, max) # returns a tuple of the minimum and maximum values
    return result