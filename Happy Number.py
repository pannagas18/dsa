n = 2

def get_out(n):
    res = map(lambda x: x**2, [int(i) for i in str(n)])
    res = (list(res))
    return(sum(res))
# count = 0
# while count < 100:
#     n = get_out(n)
#     print("n = ", n)
#     if n == 1:  
#         break
#     count += 1
# if count == 100:
#     print(False)
# else: print(True)
_set = set()
while True:
    _set.add(n)
    n = get_out(n)
    print("n = ", n)
    print(_set)
    if n == 1:
        print(True)
        break
    if n in _set:
        print(False)
        break
print(n)
