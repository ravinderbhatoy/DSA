from linkedlist import Llist


def rotate(head, k):
    """
    Rotates right by k places
    """

    if not head or not head.next:
        return head

    tail = head
    size = 1
    while tail.next:
        tail = tail.next
        size += 1

    k = k % size
    if k == size or k == 0:
        return head

    # point tail to head
    tail.next = head

    # find the node before kth node
    temp = head
    stop = size - k - 1
    while temp and stop > 0:
        temp = temp.next
        stop -= 1

    # kth node new head
    newHead = temp.next
    temp.next = None

    return newHead


nums = [1, 2, 3, 4, 5]
head = Llist(data=nums).get_head()


head = rotate(head, 3)

while head:
    print(head.data, end="->")
    head = head.next
