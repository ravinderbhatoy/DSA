def combinationSum3(k: int, n: int) -> list[list[int]]:

    candidates = []
    res = []

    def generate(target, start):
        if len(candidates) == k:
            if target == 0:
                res.append(candidates[:])
            return

        if target < 0:
            return

        for i in range(start, 10):
            if i > target:
                break
            candidates.append(i)
            generate(target - i, i + 1)
            candidates.pop()

    generate(n, 1)
    return res


k = 3
n = 9

print(combinationSum3(k, n))
