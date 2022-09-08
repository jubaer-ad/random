def threeSum(nums):
    results = []
    
    for i in range(0, len(nums) - 2):
        for j in range(1, len(nums) - 1):
            for k in range(2, len(nums)):
                if i != j and i != k and j != k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        if not len(results):
                            results.append([nums[i], nums[j], nums[k]])
                        else:
                            flag = True
                            for item in results:
                                if all(s in item for s in [nums[i], nums[j], nums[k]]):
                                    if not nums[i] == nums[j] == nums[k]:
                                        flag = False
                                    if item == [nums[i], nums[j], nums[k]]:
                                        flag = False
                            if flag == True:
                                    results.append([nums[i], nums[j], nums[k]])
    return results
# nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
# print(threeSum(nums))
print(threeSum([0,0,0,0]))