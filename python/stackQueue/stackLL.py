class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


class Stack:
    def __init__(self, size=10):
        self.topEle = None
        self.max_size = size
        self.curr_size = 0

    def push(self, val):
        if self.curr_size >= self.max_size:
            print("Overflow")
            return

        newNode = Node(val)
        newNode.next = self.topEle
        self.topEle = newNode
        self.curr_size += 1

    def top(self):
        return self.topEle.val if self.topEle else None

    def pop(self):
        if self.topEle is None:
            return None

        popped = self.topEle
        self.topEle = self.topEle.next
        self.curr_size -= 1
        return popped.val


st = Stack()
st.push(10)
st.push(20)
st.push(30)
st.push(40)
st.push(50)
st.pop()
st.pop()
print(st.top())
