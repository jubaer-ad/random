def longestCommonPrefix(strs):
#         item001 = strs[0]
#         lcp = ""
#         flag = True
#         for char in item001:
#             index = item001.index(char)
#             for item in strs:
#                 if item.index(lcp+char) + len(lcp) != index:
#                     flag = False
#                     break
#             if flag == True:
#                 lcp += char
#         return lcp
# strs = ["flowe", "flock", "flight"]
# print(longestCommonPrefix(strs))