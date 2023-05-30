class MyHashSet:
    """
    Dumb set made with a dynamic array,
    Real hashsets should be made with probing techniques.
    https://en.wikipedia.org/wiki/Hash_table
    """

    def __init__(self):
        self.set_ = []

    def add(self, key: int) -> None:
        if key not in self.set_:
            new_set = self.set_
            new_set.append(key)
            self.set_ = new_set

    def remove(self, key: int) -> None:
        if key in self.set_:
            self.set_.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.set_


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.remove(1)
param_3 = obj.contains(1)
print(param_3)
