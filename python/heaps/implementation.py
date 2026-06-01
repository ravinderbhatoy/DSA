class BinaryHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, x):
        if self.size == self.capacity:
            print("Binary heap overflow")
            return -1

        self.arr[self.size] = x
        k = self.size
        self.size += 1

        # swap to heapify
        while k != 0 and self.arr[self.parent(k)] > self.arr[k]:
            self.arr[self.parent(
                k)], self.arr[k] = self.arr[k], self.arr[self.parent(k)]
            k = self.parent(k)

    def heapify(self, ind):
        li = self.left(ind)
        ri = self.right(ind)
        smallest = ind

        if li < self.size and self.arr[li] < self.arr[smallest]:
            smallest = li

        if ri < self.size and self.arr[ri] < self.arr[smallest]:
            smallest = ri

        # if parent is not smaller swap and recurse
        if smallest != ind:
            self.arr[ind], self.arr[smallest] = self.arr[smallest],
            self.arr[ind]
            self.heapify(smallest)

    def get_min(self):
        if self.size == 0:
            return float('inf')
        return self.arr[0]

    def extract_min(self):
        if self.size == 0:
            return float('inf')
        if self.size == 1:
            self.size -= 1
            return self.arr[0]

        mini = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        self.size -= 1

        self.heapify(0)
        return mini

    # decrease key value at index i to val
    def decrease_key(self, i, val):
        self.arr[i] = val

        while i != 0 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[self.parent(i)], self.arr[i] = self.arr[i],
            self.arr[self.parent(i)]

            i = self.parent(i)

    def delete(self, i):
        # make it smallest
        self.decrease_key(i, float('-inf'))
        # remove the smallest
        self.extract_min()

    def print_heap(self):
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print()


minHeap = BinaryHeap(5)
minHeap.insert(50)
minHeap.insert(20)
minHeap.insert(40)
minHeap.insert(30)
minHeap.insert(10)

minHeap.print_heap()

print(minHeap.left(3))
