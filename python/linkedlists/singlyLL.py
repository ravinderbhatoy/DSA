class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convertToLL(nums):
    head = ListNode(nums[0])
    mover = head
    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        mover.next = node
        mover = node
    return head


def addTwoNumber(head1, head2):
    num1 = ""
    num2 = ""
    temp1 = head1
    temp2 = head2

    while (temp1 is not None and temp2 is not None):
        sm = temp1.val + temp2.val
        temp1 = temp1.next
        temp2 = temp2.next

    while (temp1 is not None):
        num1 = str(temp1.val) + num1
        temp1 = temp1.next

    while (temp2 is not None):
        num2 = str(temp2.val) + num2
        temp2 = temp2.next

    print(num1, num2)

    sm = str(int(num1) + int(num2))
    sm = sm[::-1]
    print(sm)
    head = convertToLL(sm)
    return head


nums = [2, 4, 9]
nums1 = [5, 6, 4, 9]

h1 = convertToLL(nums)
h2 = convertToLL(nums1)

head = addTwoNumber(h1, h2)
while (head is not None):
    print(head.val)
    head = head.next
