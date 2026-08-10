class RandomizedCollection:

    def __init__(self):
        self.d = collections.defaultdict(set)
        self.v = []

    def insert(self, val: int) -> bool:
        self.d[val].add(len(self.v))
        self.v.append(val)
        return len(self.d[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.d[val]:
            return False
        self.v[(i := self.d[val].pop())] = self.v[-1]
        self.d[(last := self.v.pop())].discard(len(self.v))
        i < len(self.v) and self.d[last].add(i)
        return True

    def getRandom(self) -> int:
        return random.choice(self.v)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()