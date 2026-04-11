def optimal(mat):
    n = len(mat)

    top = 0
    bottom = n-1

    while (top < bottom):
        if mat[top][bottom] == 1:
            top += 1
        else:
            bottom -= 1

    # top is potential candidate
    for i in range(n):
        if i != top and (mat[i][top] == 0 or mat[top][i] == 1):
            return -1

    return top


def bruteForce(mat):
    n = len(mat)
    # how many people they know
    out_degree = [0] * n
    # how many people known to them
    in_degree = [0] * n

    for i in range(n):
        for j in range(n):
            if i != j and mat[i][j]:
                out_degree[i] += 1
                in_degree[j] += 1

    for i in range(n):
        if out_degree[i] == 0 and in_degree[i] == n-1:
            return i

    return -1


def findCelebrity(mat: list[list[int]]) -> bool:
    n = len(mat)
    st = list()

    for i in range(n):
        st.append(i)

    while len(st) > 1:
        i = st.pop()
        j = st.pop()
        print(i, j)

        if mat[i][j] == 1:
            # i knows j so i can't be celebrity
            st.append(j)
        else:
            # i doesn't knows j so j can't be celebrity
            st.append(i)

    cel = st[-1]

    for i in range(n):
        if i != cel and (mat[cel][i] == 1 or mat[i][cel] == 0):
            return -1

    return cel


mat = [[0, 1, 0],
       [0, 0, 0],
       [1, 1, 0]]

print(findCelebrity(mat))
