from linkedlist import Llist
from linkedlist import Node


def sortLlistOf012(llist):
    temp = llist.get_head()

    if temp is None or temp.next is None:
        return temp

    zeroHead, oneHead, twoHead = Node(-1), Node(-1), Node(-1)
    zero, one, two = zeroHead, oneHead, twoHead

    while temp is not None:
        if temp.data == 0:
            zero.next = temp
            zero = zero.next
        elif temp.data == 1:
            one.next = temp
            one = one.next
        else:
            two.next = temp
            two = two.next
        temp = temp.next

    # connect lists
    if oneHead.next:
        zero.next = oneHead.next
    else:
        zero.next = twoHead.next
    one.next = twoHead.next
    two.next = None
    return zeroHead.next


nums = [2, 1, 1, 1, 2, 0, 0]
llist = Llist(data=nums)

head = sortLlistOf012(llist)
while (head is not None):
    print(head.data, end="->")
    head = head.next
print("None")
