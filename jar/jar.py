class Jar:
    def __init__(self, capacity=12):
        if not capacity < 0:
            self._capacity = capacity
        else:
            raise ValueError
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError
        elif n + self.size > self.capacity:
            raise ValueError
        else:
            self._size += n


    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

