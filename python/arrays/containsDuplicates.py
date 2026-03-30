def containsDuplicates(nums):
    myset = set(nums)
    print(len(myset))
    return len(myset) != len(nums)


nums = [1, 2, 3, 1]
print(containsDuplicates(nums))
