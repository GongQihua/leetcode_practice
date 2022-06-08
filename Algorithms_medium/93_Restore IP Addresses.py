class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def check(s):
            if not(0 <= int(s) <= 255):
                return False
            if s[0] == '0' and len(s) > 1:
                return False
            return True
        
        def dfs(s, t):
            if len(t) == 4:
                if not s:
                    ans.append('.'.join(t))
                    #print('ans =', ans)
                return
            for i in range(1, min(4, len(s) + 1)):
                #print('s=', s)
                #print('s[:i] =',s[:i])
                if check(s[:i]):
                    t. append(s[:i])
                    dfs(s[i:], t)
                    t.pop()
        ans = []
        t = []
        dfs(s, t)
        return ans

'''
思路是dfs搜索然后逐层反推
伪代码讲：
Iterate over three available slots curr_pos to place a dot.
    Check if the segment from the previous dot to the current one is valid :
        Yes :
            Place the dot.
            Check if all 3 dots are placed :
                Yes :
                    Add the solution into the output list.
                No :
                    Proceed to place next dots backtrack(curr_pos, dots - 1).
            Remove the last dot to backtrack.

以本题为例，print后的代码过程结果：
                     25525511135
IP address                              Segments
2.5.5.25511135 - not valid       [2, 5, 5]--> backtrack
2.5.52.5511135 - not valid       [2, 5, 52] --> backtrack
2.5.525.511135 - not valid       [2, 5]--> backtrack
2.55.2.5511135 - not valid       [2, 55, 2] --> backtrack
2.55.25.511135 - not valid       [2, 55, 25] --> backtrack
2.55.255.11135 - not valid       [2, 55, 255] --> backtrack
25.5.2.5511135 - not valid       [25, 5, 2] -> backtrack
25.5.25.511135 - not valid       [25, 5, 25] --> backtrack
25.5.255.11135 - not valid       [25, 5, 255] --> backtrack
25.52.5.511135 - not valid       [25, 52, 5]--> backtrack
25.52.55.11135 - not valid       [25, 52, 55] -> backtrack
2552.551.1135 - not valid        [25, 52] --> backtrack
25.525.511135 - not valid        [25] --> backtrack
255.25.511135 - not valid        [255, 2, 5] -> backtrack
255.2.55.11135 - not valid       [255, 2, 55] -> backtrack
255 2 551 1135 - not valid       [255, 2] -> backtrack
255.255.11135 - not valid        [255, 25, 5] --> backtrack
255.25.51.1135 - not valid       [255, 25, 51] --> backtrack
255.25.511.135 - not valid       [255, 25]--> backtrack
255.255.1.1135 - not valid       [255, 255, 1] --> backtrack
255.255.11.135 - valid IP        [255, 255, 11, 135] --> add to solutions
255.255.111.35 - valid IP        [255, 255, 111, 35] --> add to solutions
'''   