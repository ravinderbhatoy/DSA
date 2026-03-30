
class stack:

    def __init__(self):
        self.mini = float('inf')
        self.data = list()

    def push(self, val):
        self.mini = min(self.mini, val)
        self.data.append([val, self.mini])

    def pop(self):
        self.data.pop()
        if not len(self.data):
            self.mini = float('inf')

    def top(self):
        return self.data[-1][0]

    def getMin(self):
        return self.data[-1][1]


mystack = stack()
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.push(5)
mystack.pop()

print(mystack.getMin())
