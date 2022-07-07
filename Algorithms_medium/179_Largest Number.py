class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_list = list(map(str, nums))
        num_list.sort(key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
        return '0' if num_list[0] == '0' else ''.join(num_list)

'''
和官方答案思路是一样的，都是先转成字符串列表，再对字符串列表进行字典序降序排列。最后将列表所有字符串拼接
至于写法吗，抄的
'''