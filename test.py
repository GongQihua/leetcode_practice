def twoSum(nums, target):
        
    dict = {}
        
    for i in range(len(nums)):
        if target - nums[i] not in dict:
            dict[nums[i]] = i
        else:
            return[dict[target - nums[i]] , i]

nums = [2,4,6]
target = 8
output = twoSum(nums, target)
print(output)