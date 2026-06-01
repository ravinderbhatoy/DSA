import bisect


def longestOfLIS(nums: list[int]) -> int:
    piles = []

    for num in nums:
        print(piles)
        # bisect_left uses binary search to find the leftmost pile
        # where 'num' can be placed (or where a new pile should be created)
        idx = bisect.bisect_left(piles, num)

        # If idx equals the length of piles, it means 'num' is larger than
        # the top of all piles. We must create a new pile.
        if idx == len(piles):
            piles.append(num)
        else:
            # Otherwise, we replace the top card of that pile with 'num'
            piles[idx] = num

    # The number of piles is our answer!
    return len(piles)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(longestOfLIS(nums))
