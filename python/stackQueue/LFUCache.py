class Node:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.val = value
        self.next = next
        self.cnt = 1
        self.prev = prev


class List:
    def __init__(self):
        self.size = 0
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def addFront(self, node):
        # function to add node at the front
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node
        self.size += 1

    def removeNode(self, delNode):
        # function to remove last node
        prevNode = delNode.prev
        nextNode = delNode.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.size -= 1


class LFUCache:
    # Implementation of LFUCache
    def __init__(self, capacity: int):
        self.maxSizeCache = capacity
        self.minFreq = 0  # set minimum frequency
        self.curSize = 0  # set current frequency

        # Hashmap to store key-nodes pairs
        self.keyNode = {}
        # Hashmap to maintain lists
        # having different frequencies
        self.freqListMap = {}

    # method to update frequency of data items
    def updateFreqListMap(self, node):
        # Remove from hashmap
        del self.keyNode[node.key]

        # update the frequency list hashmap
        self.freqListMap[node.cnt].removeNode(node)

        # If node was the last node having its frequency
        if (node.cnt == self.minFreq and
                self.freqListMap[node.cnt].size == 0):
            self.minFreq += 1

        # creating a dummy list for next higher frequency
        nextHigherFreqList = List()

        # If the next higher frequency list already exist
        if node.cnt + 1 in self.freqListMap:
            # update pointer to already existing list
            nextHigherFreqList = self.freqListMap[node.cnt + 1]

        # Increment the count of data item
        node.cnt += 1

        # Add the node in front of higher frequency list
        nextHigherFreqList.addFront(node)

        # Update the frequency list map
        self.freqListMap[node.cnt] = nextHigherFreqList
        self.keyNode[node.key] = node

    # Method to get the value of key from LFU cache
    def get(self, key):
        if key in self.keyNode:
            node = self.keyNode[key]  # get node
            val = node.val  # get value

            # update the frequency
            self.updateFreqListMap(node)
            return val

        # if key not found
        return -1

    def put(self, key, value):

        # if size is 0 no items can be inserted
        if self.maxSizeCache == 0:
            return

        if key in self.keyNode:
            node = self.keyNode[key]  # get the node
            node.val = value  # update the value
            self.updateFreqListMap(node)  # update the freq

        else:
            # if cache limit is reached
            if self.curSize == self.maxSizeCache:
                # Remove the least frequently used data-item
                list = self.freqListMap[self.minFreq]
                del self.keyNode[list.tail.prev.key]
                # update frequency table
                self.freqListMap[self.minFreq].removeNode(
                    list.tail.prev
                )
                self.curSize -= 1
            self.curSize += 1  # Increment the cache size
            # Adding new value to cache and set freq to 1
            self.minFreq = 1
            # create dummy list

            listFreq = List()
            # if the list already exists
            if self.minFreq in self.freqListMap:
                # update the pointer to already present list
                listFreq = self.freqListMap[self.minFreq]

            # create node to store data item
            node = Node(key, value)

            # add the node to dummy list
            listFreq.addFront(node)

            # add to hashmap
            self.keyNode[key] = node
            # update freq list map
            self.freqListMap[self.minFreq] = listFreq


# Driver code
if __name__ == "__main__":
    # Create cache with capacity 2
    cache = LFUCache(2)

    # Put values in cache
    cache.put(1, 1)
    cache.put(2, 2)
    # Get value for key 1
    print(cache.get(1))

    # Insert another key (evicts key 2)
    cache.put(3, 3)

    # Key 2 should be evicted
    print(cache.get(2))

    # Insert another key (evicts key 1)
    cache.put(4, 4)

    # Key 1 should be evicted
    print(cache.get(1))

    # Key 3 should be present
    print(cache.get(3))

    # Key 4 should be present
    print(cache.get(4))
