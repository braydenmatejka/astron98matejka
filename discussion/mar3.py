import numpy as np
import time

def function(num):
    return num**2

def loop_speedtest(n):
    start = time.time()
    result = list(range(n))
    for i in result:
        result[i] = function(result[i])
    end = time.time()
    return end - start

def numpy_speedtest(n):
    start = time.time()
    result = np.arange(n)
    result = function(result)
    end = time.time()
    return end - start

reps = 1000000
# print(loop_speedtest(reps))
# print(numpy_speedtest(reps))

# find the unique elements in an array and
# the number of each element

newList = np.array([10, 2, 5, 10, 8, 2, 9, 8])
print(np.unique(newList, return_counts = True))

# given a 2d array, find the mean of each of the
# columns and replace each element less than
# column's mean with the mean

# ex.
# ([34, 37, 29],
# [1, 36, 41],
# [37, 34, 29],
# [1, 49, 14])

new2DArray = np.array(([34, 37, 29],
             [1, 36, 41],
             [37, 34, 29],
             [1, 49, 14]))

column_mean = np.mean(new2DArray, axis = 0)
for i in range(new2DArray.shape[1]):
    new2DArray[:, i][new2DArray[:, i] < column_mean[i]] = column_mean[i]

print(new2DArray)

