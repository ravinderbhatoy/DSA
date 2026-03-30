from linkedlist import Llist


def deleteMiddle(head):
    slow = fast = head
    prev = head

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next

    return head


nums = [1, 2]
head = Llist(data=nums).get_head()

head = deleteMiddle(head)

while head:
    print(head.data)
    head = head.next
