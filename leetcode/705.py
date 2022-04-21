# 705. Design HashSet

class MyHashSet:

    def __init__(self):
        self.set = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.set.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.set


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
print(obj.set)
obj.remove(2)
print(obj.set)
obj.add(2)
print(obj.set)
obj.remove(2)
print(obj.set)
print(obj.contains(3))
print(obj.contains(2))
