from collections import Counter


def nextGreaterElement(nums1, nums2):
    # find next greater elemens in nums2
    stack = list()
    hashmap = Counter()
    ans = []

    for i in range(len(nums2) - 1, -1, -1):
        while len(stack) and stack[-1] < nums2[i]:
            stack.pop()

        if not len(stack):
            hashmap[nums2[i]] = -1
        else:
            hashmap[nums2[i]] = stack[-1]

        stack.append(nums2[i])

    for i in range(len(nums1)):
        ans.append(hashmap[nums1[i]])

    return ans


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

print(nextGreaterElement(nums1, nums2))
