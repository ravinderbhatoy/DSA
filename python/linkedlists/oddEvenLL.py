from linkedlist import Llist


def oddEvenList(head):

    odd = head
    even = head.next
    evenCurr = even

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next

    odd.next = evenCurr
    return head


nums = [1, 2, 3, 4, 5, 6]
llist = Llist(data=nums)
head = oddEvenList(llist.get_head())
while (head is not None):
    print(head.data, end="->")
    head = head.next
print("None")
