n = int("00000010100101000001111010011100", 2)
print(n)

# n = bin(n)
n = (f'{n:032b}')
print(int(n[::-1], 2))

# print(int(n[::-1], base=2))
# p1 = 0
# p2 = len(n)-1
# while p1 < p2:
#     temp = n[p2]
#     n[p2] = p1
#     n[p1] = temp
#     p1+=1
#     p2-=1
