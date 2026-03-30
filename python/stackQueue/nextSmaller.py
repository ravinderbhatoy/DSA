def nextSmallerElement(arr, n):
    # Write your code here.
    stack = list()
    ans = [-1] * n

    for i in range(n - 1, -1, -1):
        while len(stack) and stack[-1] >= arr[i]:
            stack.pop()

        if len(stack) and stack[-1] < arr[i]:
            ans[i] = stack[-1]

        stack.append(arr[i])

    return ans


arr = [3, 3, 1, 1]
n = len(arr)

print(nextSmallerElement(arr, n))
