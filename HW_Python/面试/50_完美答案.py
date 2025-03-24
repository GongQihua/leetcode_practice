'''
考生在在线平台考试结束后,可以查看自己每道题的结果(包括题干、选项、答案、回答正确或错误),针对回答错误的题目并没有给出正确答案。这时需要综合多个考生的正确答案才能得
到一份该试卷的完美答案(即包含所有题目的正确答案)。
假设共有questionsCount 道题,题目编号从1到questionsCount。现给出每个考生的答对题目的编号,格式如
说明:
· 考生答对的题目是连续的。
· 每个考生至少答对1道题。
请计算至少需综合多少个考生的正确答案才能得到完美答案,如果无法综合到完美答案,则输出-1。
1 3
表示答对第1到3题;
表示答对第9题。
'''
def perfectAnswer(questionsCount, peopleCount, intervals):
    res = 0
    cur = 1
    i = 0
    n = peopleCount

    while cur <= questionsCount:
        max_end = -1
        while i < n and intervals[i][0] <= cur:
            max_end = max(max_end, intervals[i][1])
            i += 1
        if max_end < cur:
            return -1
        res += 1
        cur = max_end + 1
    return res

if __name__ == "__main__":
    questionsCount = int(input())
    peopleCount = int(input())
    intervals = []
    for _ in range(peopleCount):
        intervals.append(list(map(int, input().split(" "))))
    intervals.sort(key=lambda x: x[0])
    print(perfectAnswer(questionsCount, peopleCount, intervals))