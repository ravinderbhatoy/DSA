from linkedlist import Llist


def deleteDuplicates(head):
    temp = head
    while temp and temp.next:
        while temp and temp.next and temp.data == temp.next.data:
            temp.next = temp.next.next
        temp = temp.next
    return head


nums = [1, 2, 3, 3, 4, 4, 5]
head = Llist(data=nums).get_head()

head = deleteDuplicates(head)

while head:
    print(head.data, end="->")
    head = head.next
