def findMaxScore(cardPoints: list[int], k: int) -> int:
    left_sum = 0
    right_sum = 0

    for i in range(k):
        left_sum += cardPoints[i]

    max_score = left_sum

    e = len(cardPoints) - 1
    for i in range(k-1, -1, -1):
        left_sum -= cardPoints[i]
        right_sum += cardPoints[e]
        e -= 1

        max_score = max(max_score, left_sum + right_sum)

    return max_score


cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
print(findMaxScore(cardPoints, k))
