# part 1
list1to50 = []
i = 0
while i < 51:
    list1to50.append(i)
    i += 1

# TypeError: ...object is not subsriptable
# fix - i accidentally used brackets instead of parentheses in .append


# part 2
def square(list):
    list = [(i * i) for i in list]
    return list

# Failed example:
#     square([4, 5, 6])
# Expected:
#     [16, 25, 36]
# Got:
#     [4, 5, 6]
# fix - i had the line 12 as [(i * i) for i in list] without list = before

# part 3
listA = []
listB = []
for i in range(1, 11):
    listA.append(i)
for i in range(20, 31):
    listB.append(i)

oddlist = []
for i in listA:
    if i % 2 != 0:
        oddlist.append(i)
for i in listB:
    if i % 2 != 0:
        oddlist.append(i)
