'''
给你一个由若干数字（0 - 9）组成的字符串 s ，和一个整数。
如果 s 的长度大于 k ，则可以执行一轮操作。在一轮操作中，需要完成以下工作：

将 s 拆分 成长度为 k 的若干 连续数字组 ，使得前 k 个字符都分在第一组，接下来的 k 个字符都分在第二组，依此类推。注意，最后一个数字组的长度可以小于 k 。
用表示每个数字组中所有数字之和的字符串来 替换 对应的数字组。例如，"346" 会替换为 "13" ，因为 3 + 4 + 6 = 13 。
合并 所有组以形成一个新字符串。如果新字符串的长度大于 k 则重复第一步。
返回在完成所有轮操作后的 s 。
'''
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            tmp = []
            for i in range(0, len(s), k):
                val = 0
                for j in range(i, min(i+k, len(s))):
                    val += int(s[j])
                tmp.append(str(val))
            s = "".join(tmp)
        return s