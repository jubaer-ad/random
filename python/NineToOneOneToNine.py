flag = False
i = 9
test_list = list()
while i != 10:
    if i == 1:
        flag = True
        test_list.append(i)
    if flag == False:
        test_list.append(i)
        i -= 1
    else:
        test_list.append(i)
        i += 1
print(test_list)