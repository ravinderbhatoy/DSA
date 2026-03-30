from linkedlist import Llist


def removeNthFromEnd(head, n):
    if head is None:
        return head
    if head.next is None:
        return head

    slow = fast = head
    for i in range(n):
        fast = fast.next

    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    print(slow.data)
    slow.next = slow.next.next

    return head


nums = [1, 2, 3, 4, 5]
n = 2

llist = Llist(data=nums)
head = llist.get_head()

head = removeNthFromEnd(head, n)
while head is not None:
    print(head.data, end="->")
    head = head.next
print("None")
