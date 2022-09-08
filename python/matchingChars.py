def findMatch(s):
    temp_dict = dict()
    for item in s:
        if item in temp_dict:
            val = temp_dict[item]
            temp_dict[item] = val + 1
        else:
            temp_dict[item] = 1
    return temp_dict

test_string = input("Enter a string: ")
result_dict = findMatch(test_string)
for item in result_dict.keys():
    if result_dict[item] > 1:
        print(item + " - {val}".format(val = result_dict[item]))