s = "abciiidef"
k = 3
vowels = 'aeiou'
res = 0
for i in range((len(s)-k)+1):
    # output = s[i:i+k]
    # print(output.count('i'))
    output =  sum(map(s[i:i+k].lower().count, vowels))
    res = max(output, res)
print(res)