import array


class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('l', [0]*capacity)

    def _scaleup_capacity(self):
        self.capacity *= 2
        temp_array = array.array('l', [0]*self.capacity)
        for i in range(self.length):
            temp_array[i] = self.array[i]
        self.array = temp_array

    def is_empty(self):
        return not bool(self.length)

    def prepend(self, value):
        if self.length >= self.capacity:
            self._scaleup_capacity()
        if self.is_empty():
            self.array[0] = value
            self.length = 1

        for i in range(self.length, 0, -1):
            self.array[i] = self.array[i-1]
        self.array[0] = value
        self.length += 1

    def append(self, value):
        if self.length >= self.capacity:
            self._scaleup_capacity()

        self.array[self.length] = value
        self.length += 1

    def set_head(self, index):
        if index > self.length-1:
            raise IndexError
        self.length -= index
        self.capacity -= index
        self.array = self.array[index:]

    def access(self, index):
        return self.array[index]

    def insert(self, index, value):
        if self.length >= self.capacity:
            self._scaleup_capacity()
        if self.is_empty():
            if index == 0:
                self.array[0] = value
                self.length = 1
            else:
                raise IndexError
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i-1]
        self.array[index] = value
        self.length += 1

    def remove(self, index):
        if self.is_empty():
            raise Exception
        for i in range(index, self.length):
            self.array[i] = self.array[i+1]
        self.length -= 1

    def print(self):
        print([self.array[i] for i in range(self.length)])
