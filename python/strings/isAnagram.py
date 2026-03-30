def isAnagram(s1, s2):
    mapA = [0] * 26
    mapB = [0] * 26

    val = ord('a')

    for ch in s1:
        print(ch, ord(ch) - val)
        mapA[ord(ch) - val] += 1

    for ch in s2:
        mapB[ord(ch) - val] += 1

    for i in range(len(mapA)):
        if mapA[i] != mapB[i]:
            return False

    return True


s1 = "lapdmyzwvh"
s2 = "plxmrsgzjn"
print(isAnagram(s1, s2))
