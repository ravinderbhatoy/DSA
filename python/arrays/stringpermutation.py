def isFreqSame(freq1: list[int], freq2: list[int]):
    for i in range(0, 26):
        if freq1[i] != freq2[i]:
            return False
    return True


def checkInclusion(st1: str, st2: str) -> bool:
    # if st1 contains permutation of st2
    hash = [0] * 26
    for i in range(0, len(st2)):
        c = ord(st2[i]) - ord("a")
        hash[c] += 1

    win_size = len(st2)
    for j in range(0, len(st1)):
        winIdx = 0
        idx = i
        winFreq = [0] * 26
        while winIdx < win_size and idx < len(st1):
            c = ord(st1[idx]) - ord("a")
            winFreq[c] += 1
            winIdx += 1
            idx += 1

        if isFreqSame(hash, winFreq):
            return True

    return False


st1 = "ebibaooo"
st2 = "ab"

print(checkInclusion(st1, st2))
