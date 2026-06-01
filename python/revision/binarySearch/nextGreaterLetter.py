def nextGreatestLetter(letters: list[str], target: str) -> str:
    s, e = 0, len(letters) - 1
    ans = None

    while s <= e:
        mid = (s + e) // 2

        if letters[mid] > target:
            ans = letters[mid]
            e = mid - 1
        else:
            s = mid + 1

    if ans:
        return ans

    return letters[0]


letters = ["c", "f", "j"]
target = "a"
print(nextGreatestLetter(letters, target))
