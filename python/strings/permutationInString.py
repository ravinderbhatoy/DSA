def checkInclusion(s1: str, s2: str) -> bool:
    # track frequency of characters
    if len(s1) > len(s2):
        return False
    freq = [0] * 26

    def isFreqSame(freq, winFreq):
        for i in range(len(freq)):
            if freq[i] != winFreq[i]:
                return False
        return True

    for ch in s1:
        freq[ord(ch) - ord('a')] += 1

    winSize = len(s1)
    for i in range(0, len(s2) - winSize + 1):
        winFreq = [0] * 26
        for j in range(i, i + winSize):
            winFreq[ord(s2[j]) - ord('a')] += 1
        if isFreqSame(freq, winFreq):
            return True
    return False


s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))
