height = [1,8,6,2,5,4,8,3,7]

p1 = 0
p2 = p1+1
max_area = 0
while p1 < len(height)-1:
    print(p1,p2)
    if not p2>=len(height):
        h_min = min(height[p1], height[p2])
        area = h_min * (abs(p1-p2))
        p2+=1
    else:
        p1+=1
        p2=p1+1
    max_area = max(area, max_area)
print(max_area)