from collections import deque


def ladder(beginWord: str, endWord: str, wordList: list[str]) -> int:
    word_set = set(wordList)
    queue = deque([[beginWord]])
    used_on_lvl = [beginWord]  # which word was used on last level
    level = 0
    ans = []  # store all the answers

    while queue:
        path = queue.popleft()

        # Remove used words when moving to the next BFS level
        if len(path) > level:
            level += 1
            # remove all
            for word in used_on_lvl:
                word_set.discard(word)

        word = path[-1]  # last used

        # if we found the target word
        if word == endWord:
            if not ans:
                ans.append(path[:])
            elif len(ans[0]) == len(path):
                ans.append(path[:])

        # Try changing all characters of current word
        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                newWord = word[:i] + ch + word[i+1:]
                if newWord in word_set:
                    path.append(newWord)  # possible path
                    queue.append(path[:])
                    used_on_lvl.append(newWord)
                    path.pop()  # for new path

    return ans


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(ladder(beginWord, endWord, wordList))
