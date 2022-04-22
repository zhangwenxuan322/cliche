# 706. Design HashMap

class MyHashMap:

    def __init__(self):
        self.dict = {}

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value

    def get(self, key: int) -> int:
        if self.dict.get(key) is None:
            return -1
        return self.dict.get(key)

    def remove(self, key: int) -> None:
        if self.get(key):
            self.dict[key] = None


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 2)
print(obj.get(1))
obj.remove(1)
obj.put(11, 0)
print(obj.dict)
print(obj.get(11))
