def findCount(s):
    temp_dict = dict()
    for item in s:
        if item in temp_dict:
            val = temp_dict[item]
            temp_dict[item] = val + 1
        else:
            temp_dict[item] = 1
    return temp_dict

string001 = input("Enter a string: ")
result_dict = findCount(string001)
for item in result_dict.keys():
    print(item + " - {c}".format(c = result_dict[item]))
