# defining 4 functions (two for loops and two while loops)
# that find the maximum and minimum values in a list

def formin(list): # finds the minimum value using a for loop
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
    return min # returns that minimum value as an integer

def formax(list): # finds the maximum value using a for loop
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
    return max

def whilemin(list): # finds the minimum value using a while loop
    i = 0
    min = 0
    count = 0
    while i < len(list): # essentially the same as the for loops but with different syntax
        j = 0
        while j < len(list):
            if list[i] <= list[j]:
                j += 1
                count += 1
            else:
                j = len(list) + 1
                count = 0
            if count == len(list):
                min = list[i]
                i = len(list)
        i += 1
    return min

def whilemax(list): # finds the maximum value using a while loop
    i = 0
    max = 0
    count = 0
    while i < len(list): # pretty much the same as whilemin()
        j = 0
        while j < len(list):
            if list[i] >= list[j]:
                j += 1
                count += 1
            else:
                j = len(list) + 1
                count = 0
            if count == len(list):
                max = list[i]
                i = len(list)
        i += 1
    return max