from linkedlist import Llist


def reversKGroup(head, k):

    def findKthNode(head, k):
        k -= 1
        temp = head

        while k > 0 and temp:
            temp = temp.next
            k -= 1

        return temp

    def reverse(head):
        prev = next = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    temp = head
    prevNode = nextNode = None

    while temp:
        kthNode = findKthNode(temp, k)
        if not kthNode:
            if prevNode:
                prevNode.next = temp
            break

        # remove and save next link
        nextNode = kthNode.next
        kthNode.next = None

        # reverse upto kth node
        reverse(temp)

        if temp == head:
            # change head in first reverse group (kthNode)
            head = kthNode
        else:
            prevNode.next = kthNode

        prevNode = temp
        temp = nextNode

    return head


nums = [1, 2, 3, 4, 5]
head = Llist(data=nums).get_head()


head = reversKGroup(head, 3)

while head:
    print(head.data, end="->")
    head = head.next
