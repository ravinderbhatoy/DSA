def groupAnagrams(strs: list[str]) -> list[list[str]]:
    ans = []
    hashMap = dict()

    if len(strs) == 1:
        ans.append(strs)
        return ans

    for i in range(len(strs)):
        sorted_str = "".join(sorted(strs[i]))

        if hashMap.get(sorted_str) is None:
            newGroup = [strs[i]]
            ans.append(newGroup)
            hashMap[sorted_str] = len(ans) - 1
        else:
            pos = hashMap[sorted_str]
            ans[pos].append(strs[i])
    return ans


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
