class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Llist:
    def __init__(self, *args, **kwargs):
        self.head = self.tail = None
        if "val" in kwargs:
            self.push_back(kwargs["val"])
        elif "data" in kwargs:
            for val in kwargs["data"]:
                self.push_back(val)

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def push_front(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def push_back(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def pop_front(self):
        if not self.head:
            return
        self.head = self.head.next
        if not self.head:
            self.tail = None

    def pop_back(self):
        if not self.head:
            return
        # only one node
        if self.head == self.tail:
            self.head = self.tail = None
            return
        # find second to last node
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        temp.next = None
        self.tail = temp

    def insert(self, ind, val):
        if ind < 0:
            print("Index not valid")
            return
        if ind == 0:
            self.push_front(val)
            return

        cnt = 0
        temp = self.head
        while cnt < ind - 1 and temp:
            temp = temp.next
            cnt += 1
        if temp:
            newNode = Node(val)
            newNode.next = temp.next
            temp.next = newNode
            # if we inserted at the end update tail
            if newNode.next is None:
                self.tail = newNode
        else:
            print("Index not valid")

    def reverse(self):
        prev = None
        curr = self.head
        next = None

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def middle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def show(self):
        if not self.head:
            print("empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end="->")
                temp = temp.next
        print("None")

    def convert2DLL(self):
        if not self.head or not self.head.next:
            return

        prev = self.head
        curr = self.head.next

        while curr:
            curr.prev = prev
            prev = curr
            curr = curr.next


if __name__ == "__main__":
    mylist = Llist()
    mylist.push_back(10)
    mylist.push_back(20)
    mylist.push_back(30)
    mylist.push_back(40)
    mylist.push_back(50)
    mylist.push_back(60)

    print(mylist.middle())

    mylist.show()
