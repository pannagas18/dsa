s = "   fly me   to   the moon  "
_s = (s.split(' '))

a = filter(lambda c: c.isalpha(), _s)
print(list(a)[-1].__len__())
# for i in s:
#     if i.isalpha():
#         print(i)

s = s.split()
print(s)