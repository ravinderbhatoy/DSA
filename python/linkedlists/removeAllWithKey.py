from linkedlist import Llist


def deleteAllOccurences(head, key):
    temp = head
    while temp:
        if temp.data == key:
            # only one node exist and now deleted
            if not temp.next and not temp.prev:
                return None
            # first node delete
            elif not temp.prev:
                temp.next.prev = None
                head = temp.next
            # last node delete
            elif not temp.next:
                temp.prev.next = None
            else:
                print("removing middle before")
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
        temp = temp.next
    return head


nums = [10, 4, 10, 3, 5, 20, 10]
llist = Llist(data=nums)

llist.convert2DLL()
head = llist.get_head()

head = deleteAllOccurences(head, 10)

while head:
    print(head.data)
    head = head.next
