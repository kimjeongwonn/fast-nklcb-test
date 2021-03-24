### 선형큐

```python
import array


class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        if self.rear == self.capacity:
            return False  # 오버플로우
        self.array[self.rear] = value
        self.rear += 1

    def get(self):
        if self.rear == self.front:
            return False  # 언더플로우
        value = self.array[self.front]
        self.front += 1
        return value

    def peek(self):
        if self.rear == self.front:
            return False  # 언더플로우
        return self.array[self.front]

    def print(self):
        result = []
        for i in range(self.front, self.rear):
            result.append(self.array[i])
        print(result)
```

```bash
# 솔루션 결과
[]
[1, 2, 3]
1
2
3
queue underflow
None
[]
queue overflow
[4, 5]
4
5
queue underflow
None
[]

# 내 코드 결과
[]
[1, 2, 3]
1
2
3
False
[]
[4, 5]
4
5
False
[]
```

### 링크드큐

```python
class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, value):
        if self.head is None or self.tail is None:
            self.head = self.tail = Node(value, None, None)
            return True
        self.tail.next = Node(value, self.tail, None)
        self.tail = self.tail.next
        return True

    def get(self):
        if self.head is None or self.tail is None:
            return False
        target = self.head
        self.head = self.head.next
        target.next = None
        return target.value

    def peek(self):
        if self.head is None or self.tail is None:
            return False
        return self.head.value

    def print(self):
        result = []
        target = self.head
        while target:
            result.append(target.value)
            target = target.next
        print(result)
```

```bash
# 솔루션 결과
[]
[1 2 3 4 5 6 ]
1
2
3
4
[5 6 ]
[5 6 4 5 6 ]
5
6
4
[5 6 ]

# 내 코드
[]
[1, 2, 3, 4, 5, 6]
1
2
3
4
[5, 6]
[5, 6, 4, 5, 6]
5
6
4
[5, 6]
```
