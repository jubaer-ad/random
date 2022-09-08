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
for key, val in result_dict.items():
    if val == 1:
        print(key + " - " + str(val))