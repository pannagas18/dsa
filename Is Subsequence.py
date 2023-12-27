s = "abc"
t = "ahbgdc"
# s = "axc"
# t = "ahbgdc"
s = ""
t = "ahbgdc"
# s = "b"
# t = "abc"
s = list(s)
t = list(t)

# if not s:
#     print(True)
# if not t:
#     print(False)

for i in range(len(t)):
    print(i, t)
    if not s:
        print(True)
        break
    if t[i] == s[0]:
        s.pop(0)

if not s:
    print(True) 
else:
    print(False)