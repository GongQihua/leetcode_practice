'''
请你设计一个管理 n 个座位预约的系统，座位编号从 1 到 n 。
请你实现 SeatManager 类：
SeatManager(int n) 初始化一个 SeatManager 对象，它管理从 1 到 n 编号的 n 个座位。所有座位初始都是可预约的。
int reserve() 返回可以预约座位的 最小编号 ，此座位变为不可预约。
void unreserve(int seatNumber) 将给定编号 seatNumber 对应的座位变成可以预约。
'''
import heapq
class SeatManager:

    def __init__(self, n: int):
        self.available = list(range(1, n + 1))

    def reserve(self) -> int:
        return heapq.heappop(self.available)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

class SeatManager2: # 做法2
    def __init__(self, _: int):
        self.seats = 0  # 一开始没有椅子
        self.available = []

    def reserve(self) -> int:
        if self.available:  # 有空出来的椅子
            return heappop(self.available)  # 坐编号最小的
        self.seats += 1  # 添加一把新的椅子
        return self.seats

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.available, seatNumber)  # 有人离开了椅子