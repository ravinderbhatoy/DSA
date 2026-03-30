# using moore's algorithm
def majorElement(nums):
    ans = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if count == 0:
            ans = nums[i]
            count = 1
        if nums[i] == ans:
            count += 1
        else:
            count -= 1
    return ans


# Majority element 2 (find all elements appears more than n/3)
def majorElement2(nums: list[int]) -> list[int]:
    """
    find all elements that appears more than n/3
    """
    ele0 = float("-inf")
    ele1 = float("-inf")
    ans = list()
    count0 = 0
    count1 = 0
    for i in range(0, len(nums)):
        if count0 == 0 and nums[i] != ele1:
            ele0 = nums[i]
            count0 = 1
        elif count1 == 0 and nums[i] != ele0:
            ele1 = nums[i]
            count1 = 1
        elif nums[i] == ele0:
            count0 += 1
        elif nums[i] == ele1:
            count1 += 1
        else:
            count0 -= 1
            count1 -= 1

    cnt0, cnt1 = 0, 0
    for i in range(len(nums)):
        if ele0 == nums[i]:
            cnt0 += 1
        elif ele1 == nums[i]:
            cnt1 += 1

    target = len(nums) // 3
    if cnt0 > target:
        ans.append(ele0)
    if cnt1 > target:
        ans.append(ele1)
    return ans


nums = [2, 1, 1, 3, 1, 4, 5, 6]
print(len(nums) // 3)
print(majorElement2(nums))
