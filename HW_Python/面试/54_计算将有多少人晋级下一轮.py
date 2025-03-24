'''
有一个比赛，晋级下一轮的规则是：“参赛者如果得分大于0且不小于排名第K的参赛者的得分，将晋级下一轮！”
现在已知有n名参赛者(n≥k)，以及他们各自的得分，现在你需要计算将有多少人晋级下一轮。
'''
def cal_rank():
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    count = 0

    if scores[k-1] == 0:
        return 0
    
    for i in range(n):
        if scores[i] > 0 and scores[i] >= scores[k-1]:
            count += 1
    return count

if __name__ == '__main__':
    print(cal_rank())