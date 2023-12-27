str1 = "ABCABC"
str2 = "ABC"

# str1 = "ABABAB"
# str2 = "ABABB"

# x = ''
# for i, v in enumerate(list(str1)):
#     print(i, x, str1[i:]) 
#     if x == str1[i:] and str2[i:1]:
#         print("match")
#     else: 
#         x += v

# _str = min(str1, str2)
# # print(_str)
# x = ''
# for i in range(len(_str)):
#     print(i)
#     if not str1[i] == str2[i]:
#         print(str1[i])
#     else: x = _str
# print(x)

# _str = min((str1), str2)
# print(_str)
# x = ''
# if len(_str)>1:
#     if _str[:int(len(_str)/2)] == _str[int(len(_str)/2):]:
#         x = _str[:int(len(_str)/2)]
# if not x:
#     x = _str
# print(x)
# if len(str1)%len(x) == 0:
#     q = len(str1)//len(x)

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

print(gcd(len(str1), len(str2)))