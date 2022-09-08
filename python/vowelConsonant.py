vowels = ['a', 'e', 'i', 'o', 'u']
def countVC(s):
    s = s.lower()
    vowel_dict = {}
    consonant_dict = dict()
    vowel_count = 0
    consonant_count = 0
    for char in s:
        if char in vowels:
            if char in vowel_dict.keys():
                vowel_dict[char] = vowel_dict[char] + 1
            else:
                vowel_dict[char] = 1
            vowel_count += 1
        else:
            if char in consonant_dict.keys():
                consonant_dict[char] = consonant_dict[char] + 1
            else:
                consonant_dict[char] = 1
            consonant_count += 1
    return vowel_count, vowel_dict, consonant_count, consonant_dict


test_string = input("Enter a string: ")
v, vd, c, cd = countVC(test_string)
print("Vowel count: {}".format(v))
for key, val in vd.items():
    print(key + " - " + str(val))
print("Consonant count: {}".format(c))
for key, val in cd.items():
    print(key + " - " + str(val))