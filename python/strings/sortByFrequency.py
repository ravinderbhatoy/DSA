def frequencySort(s: str) -> str:
    hashmap = dict()
    freq = list()
    ans = ""

    for i in range(len(s)):
        hashmap[s[i]] = hashmap.get(s[i], 0) + 1

    for key in hashmap.keys():
        freq.append((hashmap[key], key))

    freq = sorted(freq, reverse=True)

    for i in range(len(freq)):
        st = freq[i][1] * freq[i][0]
        ans += st

    return ans


s = "abbdcc"
print(frequencySort(s))
