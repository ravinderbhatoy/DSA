def isValid(books: list, students: int, maxPagesAllowed: int) -> bool:
    pages = 0
    studentCount = 1

    for page in books:
        if page > maxPagesAllowed:
            return False
        if pages + page <= maxPagesAllowed:
            pages += page
        else:
            studentCount += 1
            pages = page

    if studentCount > students:
        return False
    else:
        return True


def allocateBooks(books: list, students: int):

    if len(books) < students:
        return -1

    st = 0
    end = sum(books)
    ans = -1

    while st <= end:
        mid = st + (end - st) // 2

        if isValid(books, students, mid):
            ans = mid
            end = mid - 1
        else:
            st = mid + 1

    return ans


print(allocateBooks([15, 17, 20], 5))
