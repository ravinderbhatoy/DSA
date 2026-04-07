def asteroidsCollision(asteroids: list[int]) -> list[int]:
    stack = list()
    for aes in asteroids:
        if (aes > 0):
            stack.append(aes)
        else:
            while len(stack) and stack[-1] > 0 and stack[-1] < abs(aes):
                stack.pop()
            # if both are equal
            if (len(stack) and stack[-1] == aes):
                stack.pop()
            elif (not len(stack) or stack[-1] < 0):
                stack.append(aes)

    return stack


asteroids = [8, -8]
print(asteroidsCollision(asteroids))
