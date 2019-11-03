class FixedDeque:
    def __init__(self, iterable, left: int = None, right: int = None):
        self.iterable = iterable
        self.left = 0 if left is None else left
        self.right = len(iterable) - 1 if right is None else right

    def pop(self):
        self.right -= 1

    def popleft(self):
        self.left += 1

    def front(self):
        return self.iterable[self.left]

    def end(self):
        return self.iterable[self.right]

    def copy(self):
        return FixedDeque(self.iterable, left=self.left, right=self.right)

    def __len__(self):
        # len = self.front - self.end + 1
        # if len < 0:
        #     print(len)
        return self.right - self.left + 1

    def __bool__(self):
        return len(self) != 0
