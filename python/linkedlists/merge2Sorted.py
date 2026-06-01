from linkedlist import Llist
from linkedlist import Node


def mergeLlist(h1, h2):
    if h1 is None or h2 is None:
        return h1 if h2 is None else h2

    if (h1.data <= h2.data):
        h1.next = mergeLlist(h1.next, h2)
        return h1
    else:
        h2.next = mergeLlist(h1, h2.next)
        return h2


def merge2Lists(h1, h2):
    dummy = Node(-1)
    mover = dummy
    while h1 and h2:
        if h1.data <= h2.data:
            mover.next = h1
            h1 = h1.next
        else:
            mover.next = h2
            h2 = h2.next
        mover = mover.next

    if h1:
        mover.next = h1
    elif h2:
        mover.next = h2

    return dummy.next


l1 = Llist(data=[1, 3, 5])
l2 = Llist(data=[1, 2, 6])

l1.show()
l2.show()

h1 = l1.get_head()
h2 = l2.get_head()

# mergeLlist(h1, h2)
merge2Lists(h1, h2)

l1.show()
