from linkedlist import Llist
from linkedlist import Node


def isPalindrome(head: Node):
    slow = head
    fast = head

    # go to middle element
    while (fast is not None and fast.next is not None):
        fast = fast.next.next
        slow = slow.next

    # revers the links
    prev = None
    curr = slow
    front = None

    while (curr is not None):
        front = curr.next
        curr.next = prev
        prev = curr
        curr = front

    # compare
    while head is not None and prev is not None:
        if (head.data != prev.data):
            return False
        head = head.next
        prev = prev.next

    return True


nums = [1, 2, 3, 3, 2, 1]
llist = Llist(data=nums)
head = llist.get_head()

print(isPalindrome(head))
