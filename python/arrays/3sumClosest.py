def threeSumClosest(nums, target) -> int:
    nums = sorted(nums)
    minDiff = float('inf')
    resultSum = 0
    for i in range(len(nums)):
        # skip same first element -> same results
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i+1
        k = len(nums) - 1

        while j < k:
            sm = nums[i] + nums[j] + nums[k]
            # no further check if target itself is found
            if sm == target:
                return target
            if sm < target:
                j += 1
            else:
                k -= 1
            diff = abs(sm - target)
            if diff < minDiff:
                resultSum = sm
                minDiff = diff
    return resultSum


nums = [1, 1, 1, 1, 1]
target = -2

print(threeSumClosest(nums, target))
print(abs(2 - 1))
