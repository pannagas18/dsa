# intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[0,15], [10,30.2], [50,70], [65,75], [70,80.1], [90,95]]
# intervals = [[1,4],[2,3]]
intervals = sorted(intervals)
# print(intervals)
# intervals_range = len(intervals)
i = 0
while i < len(intervals)-1:
    if intervals[i][-1] >= intervals[i+1][0]:
        temp = intervals[i+1]
        intervals.pop(i+1)
        val1 = min(intervals[i] + temp)
        val2 = max(intervals[i] + temp)
        intervals[i] = [val1,val2]
        i -= 1
    i += 1
print(intervals)
res = 0 
for i in intervals:
    res += i[-1]-i[0]
print(res)


# def permute(list, s):
#     if list == 1:
#         return s
#     else:
#         return [ y + x
#                  for y in permute(1, s)
#                  for x in permute(list - 1, s)
#                  ]

# print(permute(1, ["a","b","c"]))
# print(permute(3, ["a","b","c"]))
