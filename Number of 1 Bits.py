# n = int("00000000000000000000000000001011")
n = 11
# print(bin(int(n, 2)))

print(str(bin(n)).count('1'))

## EXTERNAL ##
# print((n>>12)) # right shift
res=0
for i in range(32):
    res+=(n>>i)&1
print(res)
