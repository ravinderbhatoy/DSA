class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


class Queue:
    def __init__(self, size=10):
        self.start = None
        self.max_size = size
        self.curr_size = 0
        self.end = None

    def push(self, val):
        if self.curr_size >= self.max_size:
            print("Overflow")
            return

        newNode = Node(val)
        if self.start is None:
            self.end = newNode
            self.start = newNode
        else:
            self.end.next = newNode
            self.end = newNode
        self.curr_size += 1

    def pop(self):
        if self.start is None:
            print("Underflow")
            return None

        popped = self.start.val
        self.start = self.start.next

        if self.start is None:
            self.end = None

        self.curr_size -= 1
        return popped

    def length(self):
        return self.curr_size

    def top(self):
        return self.start.val if self.start else None


queue = Queue()
queue.push(10)
queue.push(20)
queue.push(30)
queue.push(40)
queue.pop()
queue.pop()

print(queue.top())
