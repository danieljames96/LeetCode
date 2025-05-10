from heapq import heapify, heappush, heappop

class SmallestInfiniteSet:

    def __init__(self):
        self.min_int = 0
        self.added = []
        heapify(self.added)

    def popSmallest(self) -> int:
        if not self.added:
            self.min_int += 1
            return self.min_int
        else:
            return heappop(self.added)

    def addBack(self, num: int) -> None:
        if num <= self.min_int and num not in self.added:
            heappush(self.added, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)