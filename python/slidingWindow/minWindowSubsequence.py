def minWindow(s: str, t: str) -> str:
    s_len, t_len = len(s), len(t)
    s_idx, t_idx = 0, 0

    min_len = float('inf')
    start = -1

    while s_idx < s_len:
        if s[s_idx] == t[t_idx]:
            t_idx += 1

            # if we found all characters of T in order
            if t_idx == t_len:
                end = s_idx
                t_idx -= 1

                # minimize the window size by backword pass
                while t_idx >= 0:
                    if s[s_idx] == t[t_idx]:
                        t_idx -= 1
                    s_idx -= 1

                s_idx += 1
                t_idx = 0

                # update global minimum
                if end - s_idx + 1 < min_len:
                    min_len = end - s_idx + 1
                    start = s_idx

        s_idx += 1
    return "" if start == -1 else s[start: start + min_len]


def minSubsequence(s: str, t: str) -> str:
    minLen = float('inf')
    idx = 0
    m = len(t)

    for i in range(len(s)):
        idx = 0

        for j in range(i, len(s)):
            if idx < m and s[j] == t[idx]:
                # pop elements from queue in sequence
                idx += 1

            if idx >= m and j - i + 1 < minLen:
                minLen = min(minLen, j - i + 1)
                start = i
                break

    if minLen == float('inf'):
        return ""

    return s[start: start + minLen]


s = "abcdebdde"
t = "bde"

print(minSubsequence(s, t))
