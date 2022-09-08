def calculateLength(l):
    count = 0
    for item in l:
        count += 1
    return count

def rev(l):
    i = 0
    j = calculateLength(l) - 1
    while i < j:
        l[i] = l[i] + l[j]
        l[j] = l[i] - l[j]
        l[i] = l[i] - l[j]
        i += 1
        j -= 1
    return l

# array = list(range(1, 9, 1))
array = []
length = int(input("Enter length of array: "))
for i in range(0, length):
    array.append(int(input("Enter array element #{}: ".format(i))))
print("Initial array: " + str(array))
print("Reversed array: " + str(rev(array)))
