class Node:
    # doubly linked list
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.maxcapacity = capacity
        self.mpp = {}  # (key -> node)
        # head and tail of DLL
        self.head = self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, node):
        next = node.next
        prev = node.prev
        next.prev = prev
        prev.next = next

    def insertFront(self, node):
        next = self.head.next
        node.next = next
        node.prev = self.head
        self.head.next = node
        next.prev = node

    def get(self, key: int) -> int:
        if key not in self.mpp:
            return -1
        node = self.mpp[key]
        # remove old mapping
        del self.mpp[key]
        # move to front
        self.deleteNode(node)
        self.insertFront(node)
        # add new mappping
        self.mpp[key] = self.head.next
        return node.val

    def put(self, key: int, value: int) -> None:
        # if key already exist
        if key in self.mpp:
            node = self.mpp[key]
            del self.mpp[node.key]
            self.deleteNode(node)
        # if capacity reached
        if len(self.mpp) == self.maxcapacity:
            del self.mpp[self.tail.prev.key]
            self.deleteNode(self.tail.prev)
        # insert key
        node = Node(key, value)
        self.insertFront(node)
        self.mpp[key] = self.head.next


obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
