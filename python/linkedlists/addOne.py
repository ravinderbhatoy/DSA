from linkedlist import Llist
from linkedlist import Node


def addOne(head):

    def backTrack(temp):
        if not temp:
            return 1

        carry = backTrack(temp.next)
        temp.data = temp.data + carry
        if temp.data >= 10:
            temp.data = 0
            return 1
        return 0

    temp = head
    carry = backTrack(temp)
    if carry:
        newNode = Node(1)
        newNode.next = head
        head = newNode
    return head


nums = [1, 5, 2]
head = Llist(data=nums).get_head()

head = addOne(head)
while head:
    print(head.data, end="->")
    head = head.next
