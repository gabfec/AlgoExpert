#O(n) time | O(n) space
def missingNumbers(nums):
    missing = []
    all_nums = [False] * (len(nums) + 2)

    for num in nums:
        all_nums[num - 1] = True

    for i in range(len(all_nums)):
        if all_nums[i] == False:
            missing.append(i + 1)

    return missing


#O(n) time | O(1) space
def missingNumbers2(nums):
    nums += [float('inf'), float('inf')]

    for i in range(len(nums) - 2):
        idx = abs(nums[i]) - 1
        nums[idx] = -nums[idx]

    missing = []
    for i in range(len(nums)):
        if nums[i] > 0:
            missing.append(i + 1)

    return missing
