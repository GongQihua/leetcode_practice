public class Solution {
    public int MyAtoi(string s) {
        int i = 0;
        long result = 0;
        bool minus = false;
        while (i < s.Length && char.IsWhiteSpace(s[i])){
            ++i;
        }
        if (i < s.Length){
            if (s[i] == '+'){
                i+=1;
            }
            else if (s[i] == '-'){
                minus = true;
                i+=1;
            }
        }
        while (i < s.Length && char.IsDigit(s[i]))
        {
            result = result * 10 + s[i] - '0';
            if (result > int.MaxValue)
            {
                break;
            }
            ++i;
        }
        if (minus) result = -result;
        if (result > int.MaxValue)
        {
            result = int.MaxValue;
        }
        if (result < int.MinValue)
        {
            result = int.MinValue;
        }
        return (int)result;
    }
}