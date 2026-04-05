from collections import Counter, namedtuple, defaultdict, deque

# frequency dictionary
s = "aabbccczz"
my_counter = Counter(s)
print(my_counter)  # {'a': 2, ..}
print(my_counter.most_common())


# namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(-1, 4)  # (x=-1, y=4)
print(pt)

dd = defaultdict(int)  # default value will be 0
dd['a'] += 1  # like a map in cpp
dd['b'] += 2

dq = deque()
dq.append(10)
dq.append(20)
dq.appendleft(40)
dq.pop()

print(dq)
