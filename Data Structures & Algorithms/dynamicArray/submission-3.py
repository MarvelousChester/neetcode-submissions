class DynamicArray:
    def __init__(self, capacity: int):
        self.data = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = n
        self.size += 1

    def popback(self) -> int:
        last_idx = self.size - 1
        val = self.data[last_idx]
        self.data[last_idx] = None
        self.size -= 1
        return val

    def get(self, i: int) -> int:
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        self.data[i] = n

    def resize(self) -> None:
        self.capacity *= 2
        old = self.data
        self.data = [None] * self.capacity
        for i in range(len(old)):
            self.data[i] = old[i]

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
