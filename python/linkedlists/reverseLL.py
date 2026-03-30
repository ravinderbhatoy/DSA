from linkedlist import Llist


def reverseLL2(head):
    prev = nxt = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


def reverseLL(head):
    if head is None or head.next is None:
        return head

    newHead = reverseLL(head.next)

    # reverse link
    front = head.next
    front.next = head

    head.next = None

    return newHead


nums = [1, 2, 3, 4, 5]
llist = Llist(data=nums)
head = llist.get_head()

head = reverseLL2(head)

while head is not None:
    print(head.data, end="->")
    head = head.next
print("None")
