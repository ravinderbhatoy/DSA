def jobSequencing(deadline, profit):

    def find_slot(days, i):
        if days[i] == i:
            return i
        days[i] = find_slot(days, days[i])
        return days[i]

    jobs = 0
    maxProfit = 0

    # if max deadline is 4 -> [0, 1,2,3,4]
    days = list(range(max(deadline) + 1))

    profitTime = [(p, t) for p, t in zip(profit, deadline)]
    profitTime = sorted(profitTime, reverse=True)
    print(profitTime)

    for p, t in profitTime:
        av_slot = find_slot(days, t)

        if av_slot > 0:
            maxProfit += p
            jobs += 1

        # point this slot to next available slot
        days[av_slot] = av_slot - 1

    return [jobs, maxProfit]


deadline = [4, 1, 1, 1]
profit = [20, 10, 40, 30]

print(jobSequencing(deadline, profit))
