def permute(nums):
    result = []
    def backtrack(start):
        if start == len(nums):
            result.append(nums.copy())
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    backtrack(0)
    return result

if __name__ == "__main__":
    ans = permute([1,2,3,4])
    print(ans)