def firstUniqChar(s: str):
    queue = list()
    hashmap = dict()
    for i in range(len(s)):
        if hashmap.get(s[i]) is None:
            queue.append(i)
            hashmap[s[i]] = 1
        else:
            hashmap[s[i]] += 1

        while len(queue) and hashmap[s[queue[0]]] > 1:
            queue.pop(0)

    return queue[0] if len(queue) else -1


s = "dddccdbba"
print(firstUniqChar(s))
