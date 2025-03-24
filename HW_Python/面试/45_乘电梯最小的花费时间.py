'''
某公司,每天早上都有很多人去坐电梯,每个人都可能到不同的楼层.同时电梯还有一个容量限制.电梯最多只能带K个人.电梯从第a层到第b层,会花费|a-b|的时间.
 现在有N个人,以及知道每个人想要去的地方,请问如何坐电梯,才能使每个人到达到他们对应的楼层,且所花费时间最少.电梯最后要会到第1层.
'''
def min_elevator_time(N, K, floors):
    # 将楼层按升序排序
    floors.sort()
    
    total_time = 0
    # 从最高层开始，每次处理K个人
    i = N - 1
    while i >= 0:
        # 当前组的最高楼层
        highest_floor = floors[i]
        # 电梯从1层到最高层，再回到1层
        total_time += 2 * (highest_floor - 1)
        # 移动到下一个组
        i -= K
    
    return total_time

N = 5
K = 2
floors = [3,5,1,2,4]
print(min_elevator_time(N, K, floors))