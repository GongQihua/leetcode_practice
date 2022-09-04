class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return chr(257).join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split(chr(257))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
'''
方法一：使用非 ASCII 码的分隔符

Python 中可以直接 chr(257) 作为字符串的分隔符，这样就可以实现字符串的编码和解码。
时间复杂度O(n)。

方法二：编码字符串长度

编码时，将字符串的长度转成固定4位的字符串，加上字符串本身，依次拼接到结果字符串。
解码时，先取前四位字符串，得到长度，再通过长度截取后面的字符串。依次截取，最终得到字符串列表。
时间复杂度O(n)。
'''