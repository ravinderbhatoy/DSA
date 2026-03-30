def frequencySort(s: str) -> str:
    freqChars = dict()
    mylist = list()
    ans = ""

    for ch in s:
        freqChars[ch] = freqChars.get(ch, 0) + 1

    for key in freqChars.keys():
        mylist.append((freqChars[key], key))

    mylist = sorted(mylist, reverse=True)

    for pairs in mylist:
        ans += pairs[1] * pairs[0]

    return ans


s = "rtteee"
print(frequencySort(s))
