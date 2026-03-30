from linkedlist import Llist


def findPairs(head, k: int) -> [[int]]:
    left = head
    right = head
    res = []

    while right.next:
        right = right.next

    while left != right and left.prev != right:
        sm = left.data + right.data
        if sm == k:
            res.append([left.data, right.data])
            left = left.next
            right = right.prev

        elif sm > k:
            right = right.prev

        else:
            left = left.next

    return res


nums = [1, 2, 3, 4, 9]
llist = Llist(data=nums)

llist.convert2DLL()
head = llist.get_head()

k = 5
print(findPairs(head, k))
