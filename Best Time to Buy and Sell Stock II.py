prices = [7,1,5,3,6,4]

p1 = 0
p2 = p1+1
profits = 0
while p2 < len(prices):
    print(p1, p2)
    if prices[p2] < prices[p1]:
        p1 = p2
        p2 = p1+1
    else:
        profits += (prices[p2] - prices[p1])
        print(profits)
        p1 += 1
        p2 = p1+1
print(profits)