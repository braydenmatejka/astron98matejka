# part 1
fivebyfive = []
for i in range(0, 5):
    list = [5*i + j for j in range(1, 6)]
    fivebyfive.append(list)

# accidentally creted the list:
    # [[6, 7, 8, 9, 10],
    #  [11, 12, 13, 14, 15],
    #  [16, 17, 18, 19, 20],
    #  [21, 22, 23, 24, 25],
    #  [26, 27, 28, 29, 29]]
# fix - changed range(1, 6) to range(0, 5)

# part 2
i = 0
while i < len(fivebyfive):
    j = 0
    while j < len(fivebyfive[i]):
        if fivebyfive[i][j] % 3 == 0:
            fivebyfive[i][j] = '?'
        j += 1
    i += 1

# IndexError: list index out of range
#   while j < len(fivebyfive[i]):
# fix: i accidentally had lines 21 and 22 indented wrong
     
# part 3
def removeDuplicates(list):
    result = []
    count = 0
    for i in list:
        for j in list:
            if i == j:
                count += 1
        if count == 1:
            result.append(i)
        count = 0
    return result

print(removeDuplicates([1, 1, 1, 2, 3, 4, 4, 4, 5, 5]))

# kept returning an empty list, then realized my count was always >= 1 because the number itself is in the list
# changed line 37 from if count == 0: to if count == 1: