# NOT DONE

left = 1
# right = 2147483647
right = 10
res = left
for i in range(left, right+1):
    res = res&i
print(res)
