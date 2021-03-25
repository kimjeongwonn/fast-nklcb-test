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

    def print(self):
        if self.rear == self.front:
            self.result = '[]'
        else:
            self.result = '['
            for i in range(self.front, self.rear):
                self.result += str(self.array[i])+', '
            self.result = self.result[:-2] + ']'
        print(self.result)
