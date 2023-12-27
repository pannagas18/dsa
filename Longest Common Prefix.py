strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
strs = [""]
strs = ["a"]
strs = ["flower","flower","flower","flower"]
strs = ["ab", "a"]
strs = ["a","b"]

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    _len = 1
    if strs[0] == "":
        return ""

    def get_res_1(strs):
        res_1 = map(lambda word: word[:_len], strs)
        res_1 = list(res_1)
        return res_1

    while True:
        res_1 = get_res_1(strs)
        
        if not res_1.count(res_1[0]) == len(res_1):
            return strs[0][:_len-1]
        if res_1[0].__len__() == len(strs[0]):
            return strs[0][:_len]
        _len += 1
    
print(longestCommonPrefix(strs))

