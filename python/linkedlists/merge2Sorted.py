from linkedlist import Llist


def mergeLlist(h1, h2):
    if h1 is None or h2 is None:
        return h1 if h2 is None else h2

    if (h1.data <= h2.data):
        h1.next = mergeLlist(h1.next, h2)
        return h1
    else:
        h2.next = mergeLlist(h1, h2.next)
        return h2


l1 = Llist(data=[1, 3, 5])
l2 = Llist(data=[1, 2, 6])

l1.show()
l2.show()

h1 = l1.get_head()
h2 = l2.get_head()

mergeLlist(h1, h2)

l1.show()
