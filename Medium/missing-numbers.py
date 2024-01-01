def missingNumbers(nums):
    missing = []
    all_nums = [False] * (len(nums) + 2)

    for num in nums:
        all_nums[num - 1] = True

    for i in range(len(all_nums)):
        if all_nums[i] == False:
            missing.append(i + 1)

    return missing
