def twoSum(nums: [int], target: int) -> [int]:
    hashmap = dict()
    for i in range(len(nums)):
        hashmap[nums[i]] = i

    for i in range(len(nums)):
        req = target - nums[i]
        if hashmap.get(req) is not None:
            ind = hashmap[req]
            if ind != i:
                return [hashmap[req], i]

    return [-1, -1]


nums = [2, 7, 3, 1, 8, 9]
target = 12

print(twoSum(nums, target))
