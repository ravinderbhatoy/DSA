from collections import deque

"""
1. Put all words in a Set (for O(1) lookup)
2. Start BFS from beginWord with step count = 1
3. For each word in the queue:
   - Try changing each character (a-z) at every position
   - If the new word exists in the Set → add to queue, remove from Set
   - If the new word == endWord → return steps + 1
4. If queue empties → return 0
"""


def wordLadderLength(startWord, targetWord, wordList):
    st = set(wordList)
    q = deque([(startWord, 1)])

    while q:
        word, steps = q.popleft()

        # If target word is found
        if word == targetWord:
            return steps

        # Try changing every character
        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                newWord = word[:i] + ch + word[i+1:]
                if newWord in st:
                    st.remove(newWord)
                    q.append((newWord, steps + 1))
    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(wordLadderLength(beginWord, endWord, wordList))
