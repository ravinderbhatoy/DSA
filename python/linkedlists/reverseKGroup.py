from linkedlist import Llist


def reverse(head, k, size):
    prev = next = None
    curr = head

    i = 0
    while curr and i < k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i += 1

    head.next = curr
    return prev


def reversKGroup(head, k):
    size = 0
    temp = head
    while temp:
        temp = temp.next
        size += 1

    temp = head

    while size >= k:
        head = reverse(head, k, size)
        size -= k

    return head


nums = [1, 2, 3, 4, 5]
head = Llist(data=nums).get_head()

head = reversKGroup(head, 3)

while head:
    print(head.data, end="->")
    head = head.next
