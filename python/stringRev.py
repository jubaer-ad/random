def rev(s):
    tempStr = ""
    for i in s:
        tempStr = i + tempStr
    return tempStr
s = "I love Bangladesh"
print(rev(s))