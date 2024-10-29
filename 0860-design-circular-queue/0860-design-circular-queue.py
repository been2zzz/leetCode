class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.c_q = [None] * k
        self.front = 0
        self.rear = -1
        self.count = 0  # 현재 큐에 있는 요소의 개수

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.c_q[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.c_q[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.c_q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.c_q[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size
