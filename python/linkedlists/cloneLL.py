# https://leetcode.com/problems/copy-list-with-random-pointer/

# """
# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
# """

# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#       if not head:
#         return head

#       # 1. Insert copy nodes
#       temp = head
#       while temp:
#           newNode = Node(temp.val)
#           nextNode = temp.next

#           temp.next = newNode
#           newNode.next = nextNode

#           temp = nextNode

#       # 2. Assign random pointers
#       temp = head
#       while temp:
#           copyNode = temp.next
#           copyNode.random = temp.random.next if temp.random else None
#           temp = temp.next.next

#       # 3. Separate lists
#       temp = head
#       copyHead = head.next

#       while temp:
#           copyNode = temp.next
#           temp.next = copyNode.next

#           if copyNode.next:
#               copyNode.next = copyNode.next.next

#           temp = temp.next
#       return copyHead
