class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return '🍪' * self._cookies

    def deposit(self, n):
        if self._cookies + n <= self._capacity:
            self._cookies += n
        else:
            raise ValueError

    def withdraw(self, n):
        if self._cookies - n > 0:
            self._cookies -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies
