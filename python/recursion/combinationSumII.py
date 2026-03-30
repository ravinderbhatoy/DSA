def combinationSum2(candidates, target, ind, ds, ans):
    if target == 0:
        ans.append(ds[:])
        return

    if target < 0 or ind >= len(candidates):
        return

    # choice of whether to append or not
    for i in range(ind, len(candidates)):
        if i != ind and candidates[i] == candidates[i - 1]:
            continue
        if candidates[i] > target:
            break
        ds.append(candidates[i])
        combinationSum2(candidates, target - candidates[i], i + 1, ds, ans)
        ds.pop()


candidates = [1, 1, 2, 5, 6, 7, 10]
candidates = sorted(candidates)
target = 8

ans = []
combinationSum2(candidates, target, 0, [], ans)
print(ans)
