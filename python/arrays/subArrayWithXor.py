def countSubArrayWithXorK(nums: list[int], k: int) -> int:
    count = 0
    prevXors = {0: 1}
    curr_xor = 0

    for num in nums:
        curr_xor ^= num
        req = curr_xor ^ k
        if prevXors.get(req) is not None:
            count += prevXors[req]
        prevXors[curr_xor] = prevXors.get(curr_xor, 0) + 1

    return count


nums = [4, 2, 2, 6, 4]
k = 6
print(countSubArrayWithXorK(nums, k))
