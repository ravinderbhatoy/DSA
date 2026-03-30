from linkedlist import Llist
from linkedlist import Node


def addTwoNumber(head1, head2):
    t1, t2 = head1, head2
    dummyNode = Node(-1)
    curr = dummyNode
    carry = 0

    while (t1 is not None and t2 is not None):
        sm = carry
        if (t1):
            sm += t1.data
        if (t2):
            sm += t2.data

        newNode = Node(sm % 10)
        carry = sm // 10
        curr.next = newNode
        curr = curr.next

        if t1:
            t1 = t1.next
        if t2:
            t2 = t2.next

    if (carry):
        newNode = Node(carry)
        curr.next = newNode

    return dummyNode.next


list1 = Llist(data=[9, 9, 9, 9, 9, 9, 9])
list2 = Llist(data=[9, 9, 9, 9])
l1 = Llist(data=[2, 4, 3])
l2 = Llist(data=[5, 6, 4])

head = addTwoNumber(l1.head, l2.head)
while (head is not None):
    print(head.data, end="->")
    head = head.next

print("None")
