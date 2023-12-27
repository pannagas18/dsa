prices = [7,2,5,1,3,6,4]
prices = [7,6,4,3,1]
prices = [1,2]

p1 = 0
p2 = p1+1
res = 0
while p1 < len(prices)-1:
    if p2 < len(prices):
        # print(p1, p2)
        res = max(res, (prices[p2] - prices[p1]))
        p2 += 1
    else: 
        p1 += 1
        p2 = p1+1
print(res)

p1 = 0
p2 = p1+1
res = 0

while p2 < len(prices):
    print(p1, p2)
    if prices[p2] < prices[p1]:
        p1 = p2
        p2 = p1+1
    else:
        res = max(res, prices[p2] - prices[p1])
        p2  += 1
print(res)