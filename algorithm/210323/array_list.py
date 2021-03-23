import array


class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('l', [0]*capacity)

    def _scaleup_capacity(self):  # 캐퍼시티의 용량이 부족할 때 호출
        self.capacity *= 2  # 용량을 두배로
        temp_array = array.array('l', [0]*self.capacity)  # 새로운 배열 생성
        for i in range(self.length):
            temp_array[i] = self.array[i]  # 각 배열에 재할당
        self.array = temp_array  # 배열 교체

    def is_empty(self):
        return not bool(self.length)  # 빈 배열이라면 True

    def prepend(self, value):
        if self.length >= self.capacity:  # 실제 길이가 캐퍼시티보다 크거나 같다면 2배로 확장
            self._scaleup_capacity()
        if self.is_empty():  # 배열이 비어있다면 첫 번째 인덱스에 할당하고 길이 할당
            self.array[0] = value
            self.length = 1

        for i in range(self.length, 0, -1):  # 배열의 길이를 확인 한 뒤 역순으로 순회
            self.array[i] = self.array[i-1]  # 모든 요소를 인덱스+1 로 배치
        self.array[0] = value  # 0번 인덱스에 새로운 요소 할당
        self.length += 1  # 배열의 길이 늘리기

    def append(self, value):
        if self.length >= self.capacity:
            self._scaleup_capacity()

        self.array[self.length] = value  # 배열의 마지막 인덱스+1에 요소 추가
        self.length += 1  # 배열의 길이 늘리기

    def set_head(self, index):
        if index > self.length-1:  # 인덱스가 길이를 초과하면 오류
            raise IndexError
        self.array = self.array[index:]  # 배열을 해당 인덱스부터 슬라이싱해서 재할당
        self.length -= index  # 삭제된 인덱스 수 만큼 길이에서 제거
        self.capacity -= index  # 삭제된 인덱스 수 만큼 캐퍼시티에서 제거 (솔루션 참고했음)

    def access(self, index):
        return self.array[index]  # 해당 인덱스의 요소 반환

    def insert(self, index, value):
        if self.length >= self.capacity:
            self._scaleup_capacity()
        if self.is_empty():
            if index == 0:
                self.array[0] = value
                self.length = 1
            else:
                raise IndexError  # 인덱스가 비어있을 때 0번 인덱스 이외에 요소를 추가할 경우 에러
        for i in range(self.length, index, -1):  # 배열의 끝부터 해당 인덱스+1 이동
            self.array[i] = self.array[i-1]
        self.array[index] = value
        self.length += 1

    def remove(self, index):
        if index > self.length-1:  # 인덱스가 길이를 초과하면 오류
            raise IndexError
        for i in range(index, self.length):  # 해당 인덱스에 덮어쓰면서 인덱스-1 이동
            self.array[i] = self.array[i+1]
        self.length -= 1

    def print(self):
        print([self.array[i] for i in range(self.length)])
