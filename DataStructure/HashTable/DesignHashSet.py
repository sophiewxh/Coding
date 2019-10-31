class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myset = set()

    def add(self, key: int) -> None:
        self.myset.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.myset.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.myset:
            return True
        else:
            return False

if __name__ == '__main__':
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    print(obj.contains(1))
    print(obj.contains(3))
    obj.remove(2)
    print(obj.contains(2))
