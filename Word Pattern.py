# NOT DONE

pattern = "abba"
s = "dog cat cat fish"
s = "dog dog dog dog"
# pattern = "aaaa"
# s = "dog dog cat dog"
# my_dict ={}
# count = len(set(s.split()))
# for i, (p,s) in enumerate(zip(pattern, s.split())):
#     print(p, s, i, count)
#     if (s not in my_dict) and (i >= count):
#         print(s, False)
#     my_dict[s] = p

my_dict = {}
for p, s in zip(pattern, s.split()):
    print(p, s, my_dict.get(p))
    if not (my_dict.get(p) == None):
        if not (my_dict.get(p) == s):
            print(False)
    my_dict[p] = s
print(True)