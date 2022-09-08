def check_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if s1.__eq__(s2):
        return True
    else:
        if len(s1) == len(s2):
            s1_dict = {}
            s2_dict = {}
            for item in s1:
                if item in s1_dict.keys():
                    s1_dict[item] = s1_dict[item] + 1
                else:
                    s1_dict[item] = 1
            for item in s2:
                if item in s2_dict.keys():
                    s2_dict[item] = s2_dict[item] + 1
                else:
                    s2_dict[item] = 1
            for key, val in s1_dict.items():
                if key in s2_dict.keys():
                    if s2_dict[key] != val:
                        return False
                else:
                    return False
        return True

test_string001 = input("Enter string001: ")
test_string002 = input("Enter string002: ")
print("Anagram: " + str(check_anagram(test_string001, test_string002)))