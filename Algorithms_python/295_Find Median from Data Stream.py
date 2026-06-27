class MedianFinder:

    def __init__(self):
        self.queMin = list()
        self.queMax = list()

    def addNum(self, num: int) -> None:
        queMin = self.queMin
        queMax = self.queMax

        if not queMin or num <= -queMin[0]:
            heapq.heappush(queMin, -num)
            if len(queMax) + 1 < len(queMin):
                heapq.heappush(queMax, -heapq.heappop(queMin))
        else:
            heapq.heappush(queMax, num)
            if len(queMax) > len(queMin):
                heapq.heappush(queMin, -heapq.heappop(queMax))

    def findMedian(self) -> float:
        queMin = self.queMin
        queMax = self.queMax

        if len(queMin) > len(queMax):
            return -queMin[0]
        return (-queMin[0] + queMax[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()