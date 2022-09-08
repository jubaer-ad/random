def longestCommonPrefix(strs):
    shortLen = len(strs[0])
    for item in strs:
        if len(item) < shortLen:
            shortLen = len(item)

    item001 = strs[0]
    lcp = ""
    flag = True

    for i in range (0, shortLen):
        char = item001[i]
        for item in strs:
            try:
                if item.index(lcp+char) + len(lcp) != i:
                    flag = False
                    break
            except Exception as e:
                # print(e.__class__)
                flag = False
                break
        if flag == True:
            lcp += char
    return lcp

strs = ["flowe", "flock", "flight"]
print(longestCommonPrefix(strs))
strs1 = ["c", "accc", "ccc"]
print(longestCommonPrefix(strs1))
strs2 = ["Momma", "Mommy", "Mom"]
print(longestCommonPrefix(strs2))
strs3 = ["dripsfklnklsnf", "dripsodgod", "drighklgnh"]
print(longestCommonPrefix(strs3))
