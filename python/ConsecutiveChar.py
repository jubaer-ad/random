def remove_cosecutive(s, char):
    length = len(s)
    new_string = ""
    i = 0
    while i < len(s):
        flag = False
        if s[i] not in new_string:
            flag = True
        elif s[i] != new_string[-1]:
            flag = True
        if flag == True:
            new_string = "".join((new_string, s[i]))
            i += 1
        else:
            i += 1
    return new_string
print(remove_cosecutive("ssyysdeef", "char"))
print(remove_cosecutive("geeksforgeeks", "char"))

def removeConsecutiveDuplicates(s):
    if len(s)<2:
        return s
    if s[0]!=s[1]:
        return s[0]+removeConsecutiveDuplicates(s[1:])
    return removeConsecutiveDuplicates(s[1:])
print(removeConsecutiveDuplicates("ssyysdeef"))
print(removeConsecutiveDuplicates("geeksforgeeks"))
