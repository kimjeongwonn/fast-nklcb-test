import array


class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('l', [0]*capacity)

    def __scaleup_capacity(self, value=None, index=None):  # 캐퍼시티의 용량이 부족할 때 호출
        self.capacity *= 2  # 용량을 두배로 (솔루션 참고했음)
        temp_array = array.array('l', [0]*self.capacity)  # 새로운 배열 생성
        if value is not None and index is not None:
            for i in range(0, index):
                temp_array[i] = self.array[i]  # 지정인덱스 -1까지 재할당
            for i in range(index+1, self.length+1):  # 지정인덱스 +1부터 재할당
                temp_array[i] = self.array[i-1]
            temp_array[index] = value  # 지정인덱스에 값 할당
            self.array = temp_array  # 배열 교체
            self.length += 1
        else:
            for i in range(self.length):
                temp_array[i] = self.array[i]  # 각 배열에 재할당
            self.array = temp_array  # 배열 교체

    def is_empty(self):
        return not bool(self.length)  # 빈 배열이라면 True

    def prepend(self, value):
        if self.length >= self.capacity:  # 실제 길이가 캐퍼시티보다 크거나 같다면 2배로 확장
            self.__scaleup_capacity()

        for i in range(self.length, 0, -1):  # 배열의 길이를 확인 한 뒤 역순으로 순회
            self.array[i] = self.array[i-1]  # 모든 요소를 인덱스+1 로 배치
        self.array[0] = value  # 0번 인덱스에 새로운 요소 할당
        self.length += 1  # 배열의 길이 늘리기

    def append(self, value):
        if self.length >= self.capacity:
            self.__scaleup_capacity()

        self.array[self.length] = value  # 배열의 마지막 인덱스+1에 요소 추가
        self.length += 1  # 배열의 길이 늘리기

    def set_head(self, index):
        if index > self.length-1:  # 인덱스가 길이를 초과하면 오류
            raise IndexError
        self.array = self.array[index:]  # 배열을 해당 인덱스부터 슬라이싱해서 재할당
        self.length -= index  # 삭제된 인덱스 수 만큼 길이에서 제거
        self.capacity -= index  # 삭제된 인덱스 수 만큼 캐퍼시티에서 제거 (솔루션 참고했음)

    def access(self, index):
        return self.array[index]

    def insert(self, index, value):
        if self.is_empty():
            if index == 0:
                self.array[0] = value
                self.length = 1
            else:
                raise IndexError  # 인덱스가 비어있을 때 0번 인덱스 이외에 요소를 추가할 경우 에러

        if self.length >= self.capacity:
            # 확장해야 한다면 값과 인덱스를 전달하여 복사를 한 번만 해서 진행
            self.__scaleup_capacity(value, index)
        else:
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
        print(self.array.tolist())
