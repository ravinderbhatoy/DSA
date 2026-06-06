from collections import Counter


def isNStraightHand(hand: list[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False

    count = Counter(hand)

    hand.sort()

    for card in hand:
        # card already used
        if count[card] == 0:
            continue

        for i in range(groupSize):
            current = card + i

            if count[current] <= 0:
                return False

            count[card] -= 1
    return True


nums = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
print(isNStraightHand(nums, groupSize))
