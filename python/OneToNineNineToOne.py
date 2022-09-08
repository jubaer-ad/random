flag = False
i = 1
test_list = list()
while i != 0:
    if i == 9:
        flag = True
        test_list.append(i)
    if flag == False:
        test_list.append(i)
        i += 1
    else:
        test_list.append(i)
        i -= 1
print(test_list)
        