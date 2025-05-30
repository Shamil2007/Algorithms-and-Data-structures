from typing import Any, Optional

class MyArray:
    def __init__(self, length: int = 0, data: Optional[dict] = None):
        if data is None:
            data = {}  # Using dict to simulate sparse array
        self.length: int = length
        self.data: dict[int, Any] = data

    def get(self, index: int):
        return self.data.get(index, None)  # Safely get value or return None if not found

    def append(self, item: Any) -> int:
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self) -> Any:
        if self.length == 0:
            raise IndexError("pop from empty MyArray")
        last_index = self.length - 1
        item = self.data[last_index]
        del self.data[last_index]
        self.length -= 1
        return item

    def insert(self, index: int, item: Any) -> None:
        if index < 0 or index > self.length:
            raise IndexError("insert index out of range")
        # Shift elements to the right
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = item
        self.length += 1

    def delete(self, index: int) -> Any:
        if index < 0 or index >= self.length:
            raise IndexError("delete index out of range")
        item = self.data[index]
        # Shift elements to the left
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1
        return item

    def __str__(self) -> str:
        # Generate a list-like string from the dict (in order)
        elements = [self.data.get(i, None) for i in range(self.length)]
        return f"MyArray(length={self.length}, data={elements})"

# Usage
arr = MyArray()
arr.append(5)
arr.append(10)
arr.append(15)
print(arr)  # MyArray(length=3, data=[5, 10, 15])
arr.pop()
print(arr)  # MyArray(length=2, data=[5, 10])
arr.insert(1, 20)
print(arr)  # MyArray(length=3, data=[5, 20, 10])
deleted = arr.delete(1)
print(f"Deleted value: {deleted}")  # Deleted value: 20
print(arr)  # MyArray(length=2, data=[5, 10])
