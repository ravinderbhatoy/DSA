def combinationSum(candidates: [int], ind: int, target: int, ds: [int], ans: [[int]]):
    if target == 0:
        ans.append(ds[:])
        return

    if target < 0 or ind == len(candidates):
        return

    for i in range(ind, len(candidates)):
        ds.append(candidates[i])
        combinationSum(candidates, i, target - candidates[i], ds, ans)
        ds.pop()


candidates = [2, 3, 6, 7]
target = 7
ans = []
combinationSum(candidates, 0, target, [], ans)
print(ans)
